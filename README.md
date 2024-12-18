# RE-DACT: A Secure and Customizable Redaction Tool

## Overview

RE-DACT is a cutting-edge solution designed to address the growing need for secure handling of sensitive information. Developed for institutions and government organizations, this tool offers customizable redaction options across multiple file types, ensuring data privacy, compliance, and scalability. Leveraging advanced technologies like Blockchain, NLP, and GenAI, RE-DACT combines transparency, security, and user-friendliness.

## Project Details

## Prepared For:
**National Technical Research Organisation (NTRO), SIH 2024 PS - 1678**

## Team Members:

**Varad Joshi**

**Soham Penshanwar**

**Rasika Thakur**

**Pratiksha Khandbahale**

**Dhanashri Patil**

**Rajesh Khavane**

## Features

- **Customizable Redaction Levels**: User-defined options for secure sharing across various recipients.

- **Multi-Format Support**: Text, images, and videos.

- **Security-Focused**: Blockchain and SHA-256 hashing for integrity and secure data handling.

- **Offline Functionality**: Ensures complete privacy and control over data.

- **User-Friendly**: Designed for both technical and non-technical users.


## Frontend

Technologies: HTML, CSS, JavaScript.

**Features:**

File upload module.

Redaction level sliders (increments by 25%).

Redaction type options: blur, black out, or replace.

Preview functionality for user review.

Google OAuth integration for authentication.

## Backend

Technologies: Python, FastAPI (web), Tauri (desktop).

**Capabilities:**

File processing and redaction logic.

Blockchain integration using Python libraries like web3.py.

User session security with JWT authentication.

Redaction Engine

Text: NLP models (Spacy, PyTorch) to identify and redact sensitive information.

Images and Videos: OpenCV and GAN models for redaction.

Synthetic Data: TensorFlow-based GenAI for anonymized replacements.

Security Mechanisms

SHA-256 Hashing: Ensures data integrity during processing.

Blockchain: Ethereum for transaction logs and IPFS for secure storage.

JWT Authentication: Protects user sessions.

Implementation Workflow

Input: User uploads a document (PDF, image, or video).

Processing: Redaction engine processes the file based on user settings.

Output: Redacted document is presented for review and download.

Results and Evaluation

Performance Metrics

## Accuracy:

Text Redaction: **98%** precision.

Video Redaction: **95%** success rate.

## Efficiency:

Text Processing: **~5 seconds**.

Video Processing: **~15 seconds**.

## User Feedback: High usability and effectiveness ratings.

## Learning Outcomes

Mastery in blockchain integration for secure data handling.

Enhanced expertise in GenAI models for synthetic data generation.

Developed a scalable and modular architecture.

## Future Scope

- **Cloud Integration:** Optional cloud storage for enhanced scalability.

- **Language Expansion:** Support for multiple languages in NLP models.

- **Mobile Application:** Develop a mobile version for on-the-go redaction.

- **Advanced GenAI:** Improved synthetic data models for contextual relevance.

## Installation

**Prerequisites**

Python 3.8+

Node.js

Tauri

Steps

**Clone the repository.**
```bash
git clone https://github.com/Diplomats-SIH/RE-DACT.git
```


Navigate to the project directory.
```bash
cd RE-DACT/REDACT_Main/SIH/SIH_Main
```
Install dependencies.
```bash
pip install -r requirements.txt
```

## References

Python Documentation

OpenCV Library

Blockchain Basics

TensorFlow for GenAI
