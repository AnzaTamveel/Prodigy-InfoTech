from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        source_ip = ip_layer.src
        destination_ip = ip_layer.dst
        protocol = ip_layer.proto

        # Determine protocol
        if packet.haslayer(TCP):
            protocol_name = "TCP"
        elif packet.haslayer(UDP):
            protocol_name = "UDP"
        else:
            protocol_name = "Other"

        # Print packet information
        print(f"Source IP: {source_ip}")
        print(f"Destination IP: {destination_ip}")
        print(f"Protocol: {protocol_name}")

        # Optionally print some payload data
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = packet.payload
            if len(payload) > 0:
                print(f"Payload (first 50 bytes): {bytes(payload)[:50]}")

        print("=" * 50)

def main():
    print("Starting packet sniffer. Press Ctrl+C to stop.")
    try:
        sniff(prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print("Packet sniffer stopped.")


if __name__ == "__main__":
    main()
