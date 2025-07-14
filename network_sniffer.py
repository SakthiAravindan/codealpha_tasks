from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):
        ip_layer = packet["IP"]
        print(f"Source: {ip_layer.src} → Destination: {ip_layer.dst} | Protocol: {ip_layer.proto}")

print("Starting Packet Sniffer...") 
sniff(prn=packet_callback, count=10)
