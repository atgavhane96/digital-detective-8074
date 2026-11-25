# Mission 07 — How Computers Communicate

## 1. Task / objective
The objective of Mission 7 is to understand core computer networking concepts (LAN, MAN, WAN, DNS, routers, protocols, packet switching, client-server architecture), execute safe Terminal network connectivity and DNS lookup tests, and explain the step-by-step communication sequence when loading a website.

---

## 2. Work completed

### Task 7.1 — Explain Network Concepts

| Concept | Explain it in your own words | Example |
|---|---|---|
| **LAN** | A Local Area Network connects devices within a tightly limited physical boundary, such as a single room, home, or school computer lab, enabling fast local file and printer sharing. | Devices connected to a home Wi-Fi router or computers wired in a university lab. |
| **MAN** | A Metropolitan Area Network interconnects multiple LANs across a wider city or sprawling campus area, typically utilizing high-speed fiber-optic links. | A university network connecting separate department buildings across a campus, or city-wide municipal Wi-Fi. |
| **WAN** | A Wide Area Network spans vast geographical regions—crossing cities, countries, or continents—to link distant LANs and MANs together. | The global Internet, or a multinational corporation's private network connecting offices in India and the US. |
| **DNS** | The Domain Name System acts like the Internet's directory, translating human-readable domain names into numerical IP addresses that network hardware uses for routing. | Translating `example.com` into its numerical IPv4 address (`172.66.147.243`). |
| **Router** | A networking hardware device that connects different networks together and examines packet headers to forward data along optimal paths toward their destination. | A home wireless router bridging the private local home network with the Internet Service Provider (ISP) network. |
| **Protocol** | A formal set of standardized rules and message formats that devices must obey to reliably encode, transmit, receive, and interpret data across a network. | `HTTP/HTTPS` for loading web pages, `TCP/IP` for reliable packet delivery, or `ICMP` for connectivity pings. |
| **Packet Switching** | A transmission technique where large data messages are split into small numbered packets that can travel independently over shared network routes and reassemble accurately at the destination. | Streaming a video or downloading a webpage where chunks travel across varying router hops before reassembly in your browser. |
| **Client-Server** | A communication model where a requesting device (the client) initiates requests for resources or services, and a dedicated host (the server) listens for, processes, and fulfills those requests. | A web browser (client) requesting an HTML webpage from a remote web server (server). |

---

### Task 7.2 — Observe Network Information

#### 1. Connectivity Test (`ping -c 3 example.com`)
Executed a 3-packet ICMP echo test to `example.com`:
- **Observed Result**: 3 packets transmitted, 3 packets received, 0.0% packet loss, round-trip latency averaging ~7.3 ms.
- **What a connectivity test helps check**: It verifies whether a live network path exists between my computer and a remote destination host, confirming local network access, DNS resolution, packet routing, and approximate round-trip network latency.

#### 2. DNS Lookup (`nslookup example.com`)
Queried the Domain Name System for `example.com`:
```text
Server:         [redacted-resolver]
Address:        [redacted-resolver]#53

Non-authoritative answer:
Name:   example.com
Address: 104.20.23.154
Name:   example.com
Address: 172.66.147.243
```
- **What information a DNS lookup displays**: It displays the DNS resolver server that answered the query and the resolved public IP address(es) mapped to the queried domain name.
- **Role of DNS when entering a website name in a browser**: Humans remember readable names like `example.com`, whereas network routers only route traffic using numerical IP addresses. When a URL is entered into a browser, the OS and browser query DNS first to retrieve the server's exact IP address before any webpage data can be requested.

*(Note: Personal local IP addresses, Wi-Fi SSIDs, and private resolver details have been redacted).*

---

### Task 7.3 — What Happens When You Open a Website?

1. **User Action on the Client**: You type a web address (such as `https://example.com`) into your web browser, which acts as the **client** software.
2. **DNS Resolution**: The client does not yet know where the site lives numerically, so it sends a **DNS** query through your local **router** to translate `example.com` into the remote **server**'s IP address.
3. **Establishing a Connection via Protocols**: Once the IP address is returned, the client initiates a reliable connection with the remote web server using standard network **protocols** (**TCP/IP** and **TLS** for encrypted HTTPS communication).
4. **Routing Requests Across Networks**: The client sends an **HTTP/HTTPS** GET request divided into small data packets. Your local router forwards these packets across ISP networks and intermediate routers toward the destination IP.
5. **Server Processing**: The remote **server** receives the request packets, reassembles them, processes what webpage resource was requested, and prepares an HTTP response containing the HTML, CSS, and media data.
6. **Receiving and Rendering Response**: The server transmits response packets back across the network to your client device, where the browser reassembles the data and renders the interactive webpage on your screen.

---

## 3. Commands / tools used
- `ping -c 3 example.com`: Tested network reachability and packet round-trip time (RTT).
- `nslookup example.com`: Queried DNS records to inspect domain-to-IP address mapping.

## 4. My understanding
- Internet communication depends on layered abstraction: DNS handles naming, routers and packet switching handle physical delivery across networks, and protocols like TCP and HTTP/HTTPS govern how clients and servers interpret messages reliably.

## 5. Difficulties faced
- Distinguishing between local network device addresses and public destination server IP addresses in terminal output.

## 6. How I resolved them
- Carefully verified that only public `example.com` resolution records were documented and redacted local resolver addresses to maintain privacy.

## 7. Evidence / files
- [README.md](README.md) in `mission-07-networking/`

## 8. Commit details
- Commit message: `Explain networking concepts and website communication`
- Gate condition: Ready for staging, commit, and remote push.
