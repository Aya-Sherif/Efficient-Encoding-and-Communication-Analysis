# Efficient Encoding and Communication Analysis

This repository contains an analysis and implementation of encoding schemes and their impact on communication systems. The project explores methods like Huffman Coding, Shannon-Fano Encoding, and Hamming Codes. It also evaluates their efficiency in noisy channels using metrics such as Bit Error Rate (BER) vs. Signal-to-Noise Ratio (SNR).

## Team Members
- **Aser Osama** 
- **Aya Sherif**
- **Mariam Ismael** 
- **Salma Hatem**

## Project Overview

The project is divided into the following parts:
1. **Character Probability Calculation and Entropy Estimation**: Calculates the entropy of English characters and analyzes fixed-length coding.
2. **Huffman Encoding and Decoding**: Includes implementation of Huffman trees for encoding and decoding text files.
3. **Shannon-Fano Encoding**: Another efficient encoding technique evaluated for performance.
4. **Hamming Code Implementation**: Incorporates error-detecting and error-correcting codes to enhance communication robustness.
5. **Bit Error Rate (BER) vs. Signal-to-Noise Ratio (SNR)**: Simulates and evaluates encoding schemes under varying noise levels.
6. **End-to-End Communication System**: Integrates encoding, noise addition, and decoding to evaluate overall system performance.

## Key Features
- Comparison of Huffman, Shannon-Fano, and Fixed-Length coding schemes.
- Efficiency analysis of each encoding method.
- Noise resilience testing using Hamming Code in simulated communication channels.
- Visualized results for BER vs. SNR using Matplotlib.

## Usage
### Prerequisites
- Python 3.7+
- Libraries: `numpy`, `matplotlib`

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Efficient-Encoding-and-Communication-Analysis.git
   cd Efficient-Encoding-and-Communication-Analysis
### Results
- Comprehensive comparison of encoding techniques.
+ Graphical representation of BER vs. SNR with and without Hamming Codes.
- Insights into the efficiency and resilience of encoding methods in noisy environments.
