# CS471 – Web Technologies
## Laboratory Report
## Lab 1: The Internet Protocols

**Student Name:** Razan Alrasheed  
**Student ID:** 431217653

---

# Part 1: Capturing HTTP Traffic

Wireshark was used to capture traffic while accessing an HTTP website. The display filter `http` was then applied to isolate HTTP packets.

![Figure 1. HTTP traffic](Figure%201.%20HTTP%20traffic.png)

*Figure 1. HTTP traffic filtered in Wireshark. Packet 4160 contains GET /online HTTP/1.1.*

## HTTP Request and Response Analysis

| Item | Observed Value |
| --- | --- |
| Request method | GET |
| Requested path | /online |
| First response | HTTP/1.1 301 Moved Permanently |
| Redirected request | GET /online/ HTTP/1.1 |
| Successful page response | HTTP/1.1 200 OK (text/html) |
| Additional request | GET /favicon.ico HTTP/1.1 |
| Favicon response | HTTP/1.1 200 OK (PNG) |

Observation: The browser first requested /online. The server returned 301 Moved Permanently, so the browser sent another GET request for /online/. The server then returned 200 OK. A separate GET request was also sent for the website favicon, which was returned as a PNG image.

![Figure 2. HTTP request response sequence](Figure%202.%20HTTP%20request%20response%20sequence.png)

*Figure 2. HTTP request/response sequence showing 301 redirect, 200 OK, and favicon retrieval.*

---

# Part 2: Analyzing TCP/IP Traffic

The HTTP connection was isolated using TCP stream 38. The same stream shows connection establishment, data exchange, and connection termination between 192.168.8.11:41936 and 34.223.124.45:80.

## TCP Stream Conversation

![Figure 3. Follow TCP Stream](Figure%203.%20Follow%20TCP%20Stream.png)

*Figure 3. Follow TCP Stream showing the HTTP conversation between the client and server in TCP stream 38.*

The Follow TCP Stream view displays the complete HTTP conversation for TCP stream 38, including GET /online, the HTTP/1.1 301 Moved Permanently response, the redirected GET /online/ request, and the HTTP/1.1 200 OK response.

## TCP Three-Way Handshake

![Figure 4. TCP stream 38](Figure%204.%20TCP%20stream%2038..png)

*Figure 4. TCP stream 38. The first packet is the SYN and the packet list also shows SYN-ACK and ACK.*

| Packet | Direction | Flags | Seq | Ack |
| --- | --- | --- | --- | --- |
| 4062 | Client → Server | SYN | 0 | 0 |
| 4119 | Server → Client | SYN, ACK | 0 | 1 |
| 4120 | Client → Server | ACK | 1 | 1 |

The SYN initiates the connection. The server replies with SYN-ACK, and the client completes the three-way handshake with ACK. The sequence and acknowledgment numbers confirm the expected TCP handshake progression.

## TCP Data Transfer

![Figure 5. TCP data transfer](Figure%205.%20TCP%20data%20transfer.png)

*Figure 5. TCP data transfer associated with the HTTP exchange; TCP sequence and acknowledgment information is visible.*

After the connection was established, data was exchanged using TCP segments. TCP sequence numbers identify the byte position in the stream, while acknowledgment numbers indicate the next byte expected by the receiver.

## TCP Termination

![Figure 6. TCP termination](Figure%206.%20TCP%20termination.png)

*Figure 6. TCP termination. Packet 4269 contains FIN, ACK and packet 4270 contains the final ACK.*

The server initiated termination with FIN, ACK (packet 4269). The client acknowledged it with ACK (packet 4270), completing the observed connection termination.

---

# Part 3: Capturing and Analyzing UDP Traffic

UDP traffic was generated and captured, then the display filter `udp` was applied. A UDP packet was selected to inspect its header fields and payload.

![Figure 7. UDP packet details](Figure%207.%20UDP%20packet%20details.png)

*Figure 7. UDP packet details showing source port, destination port, length, UDP payload, and data.*

| Observed field | Value |
| --- | --- |
| Packet number | 12141 |
| Source port | 443 |
| Destination port | 60360 |
| UDP length | 41 bytes |
| UDP payload | 33 bytes |
| Data | 33 bytes |

## UDP Header Compared with TCP

UDP has a simpler header than TCP. The UDP header mainly contains source port, destination port, length, and checksum. TCP includes additional fields for sequence numbers, acknowledgments, flags, window control, and connection management. This makes UDP lower-overhead, while TCP provides connection-oriented reliability and ordering.

---

# Part 4: Comparing TCP and UDP

## Task 1: Reliability, Connection Establishment, Integrity, and Ordering

| Criteria | TCP or UDP | Reason |
| --- | --- | --- |
| Reliability and Connection Establishment | TCP | TCP establishes a connection using the three-way handshake and uses acknowledgments and retransmission mechanisms to support reliable delivery. |
| Data Integrity and Ordering | TCP | TCP uses sequence and acknowledgment numbers so received data can be tracked and reassembled in the correct order. |

## Task 2: Use Cases and Performance

| Criteria | TCP | UDP |
| --- | --- | --- |
| Use Cases | Web browsing (HTTP/HTTPS), email, and file transfer. | Streaming media, VoIP, DNS, and real-time online applications/games. |
| Performance | Generally has more overhead because of connection setup, acknowledgments, ordering, and reliability mechanisms. | Generally has lower overhead because it does not require connection establishment or TCP-style acknowledgment and retransmission mechanisms. |

**Conclusion:** The capture demonstrates the main differences between the two transport protocols. TCP provides connection establishment, sequencing, acknowledgments, and controlled termination. UDP uses a smaller and simpler transport header and is suitable when low overhead and timeliness are more important than TCP-style reliability.
