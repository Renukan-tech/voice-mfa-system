# VoiceM3F - Multi-Factor Voice Authentication System

## Overview

VoiceM3F is a multi-factor authentication system that enhances login security by combining traditional password authentication, voice recognition, and One-Time Password (OTP) verification.

The system uses the user's voice as an additional authentication factor. If voice authentication fails multiple times, the system automatically switches to OTP verification to securely verify the user's identity.

## Features

* User registration and login
* Password-based authentication
* Voice-based user verification
* Multi-factor authentication (MFA)
* OTP fallback mechanism
* Secure login workflow
* Failed attempt monitoring
* Enhanced account protection

## Authentication Workflow

1. User enters username and password.
2. System verifies credentials.
3. User records a voice sample.
4. Voice sample is compared with the registered voice profile.
5. If voice authentication succeeds, access is granted.
6. If voice authentication fails three consecutive times:

   * OTP verification is triggered.
   * OTP is sent to the registered contact.
   * User must verify the OTP to gain access.

## Technologies Used

* HTML
* CSS
* JavaScript
* Node.js
* Voice Recognition Processing
* OTP Verification System

## Security Features

* Multi-factor authentication
* Voice biometric verification
* OTP-based recovery mechanism
* Failed login attempt tracking
* Enhanced protection against unauthorized access

## Applications

* Secure login systems
* Banking applications
* Enterprise authentication
* Personal account security
* Identity verification systems

## Future Enhancements

* AI-based speaker recognition
* Liveness detection
* Mobile application support
* Face recognition integration
* Advanced voice matching algorithms
* Cloud-based authentication services

## Learning Outcomes

This project demonstrates:

* Authentication system design
* Multi-factor authentication concepts
* Voice-based verification
* Web development
* Security implementation techniques

## Author

Developed as a cybersecurity and authentication mini project.
