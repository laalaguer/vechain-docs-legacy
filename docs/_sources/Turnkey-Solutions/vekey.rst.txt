VeKey based Secure Identity Turnkey Solution
================================================

.. toctree::
   :maxdepth: 1

   vekey/mac.md
   vekey/windows.md

Vekey, a new standard in security for the VeChain ecosystem, is a comprehensive turnkey solution that is comprised of VeKey hardware and VeKey Bridge software. As a specially designed secure identity solution for asset management, VeKey boasts superior security to current market offerings. 

##VeKey Hardware

VeKey is an easy to use, certified secure hardware solution for the storage of private keys and the management of digital signatures and identities. It is a specially designed identity hardware device for asset management that boasts superior security to current market offerings. Get [VeKey Manual](doc:quick-guide-vekey-v20)  on how to manage your VeKey.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/807daec-VeKey.jpeg",
        "VeKey.jpeg",
        1920,
        1080,
        "#d5cdcc"
      ]
    }
  ]
}
[/block]
VeKey provides an optimal experience within VeChain Ecosystem by offering the following features:
- Internationally Recognized Certifications
VeKey comes embedded with a secure MCU (ARM SecurCore SC3000) endowed with CC EAL4+ certification, the same certification standard used in Bank card chip products. 

- Data Security Protection
VeKey features multiple complimentary security layers, including compulsory double authentication (biometric identification via fingerprint + PIN), software-based security mechanism, and remote back-end verification. 

- Simplicity
Through VeKey, transactions can be authorized easily: just press your finger on the device and enter the PIN. 

- Multi-signature
Private keys can be broken down into multiple pieces through VeKey, thus enabling offline threshold multi-signature. To sign a transaction, you'd need the pre-defined number of VeKeys to recover the private key and sign.

##VeKey Bridge

Once VeKey hardware is ready, you need to use the VeKey Bridge Tool connect VeKey with web application. Through restful api, you can get VeKey serial number list, public information (address, public key), device information (hardware version, firmware version, alias), signature of VeKey. 

Choose to download VeKey Bridge installation package and User Manual for your applications:
MAC OS: 
[VeKeyBridge.dmg](http://bbs-prd.oss-cn-hongkong.aliyuncs.com/c6f9d160-154f-4ece-b61d-afeaca6f2c9a.dmg)   
[VeKey Bridge Tool Manual (Mac)](doc:vekey-bridge-tool-manual-mac) 

Windows: 
[VeKeyBridge 1.0.2 Setup.exe](http://bbs-prd.oss-cn-hongkong.aliyuncs.com/9eed11b2-109e-490c-b934-fd820370f8a7.exe) 
[VeKey Bridge Tool Manual (Windows)](doc:vekey-bridge-tool-manual-windows) 

If you are interested in following documents, please Email [bd@vechain.com](mailto:bd@vechain.com).

-VeKey Bridge SDK Quick Start: guide on how to import the VeKeyBridgeSDK to your project, and configure your Visual Studio environment. 

-VeKey Bridge Restful API: the VeKey Bridge Restful API document lists all the RESTful APIs VeKey Bridge offered. 

-VeKey Bridge SDK API: the VeKey Bridge SDK API document lists all the VeKeyBridgeSDK native APIs. 

-VeKeyBridgeSDK: the VeKeyBridgeSDK resource package for Windows or Mac OS.

-VeKeyBridgeSDKSample: the demo code how to use VeKeyBridgeSDK.

-VeChain certificate and signature generation: VeChain certificate file requests and CSR document generation.

-Cert_sample: the java sample for certificate verification.


##Use Cases
This turnkey solution can be used to further develop into a secure product which can be run as a SaaS product to serve both retail and enterprises clients. 
•	On-chain ecosystem management: In Digital Carbon Ecosystem, VeKey is used by DNV GL, the independent third party, to perform parameter modification, data authentication, and credit issuing.
•	On-chain KYC: In the case of VeVID, VeKey is used to validate, audit, and check system users, and each validated user will be assigned a unique ID on the blockchain.
•	Digital Asset Management: In the case of off-chain threshold signature solution, private keys can be broken down into multiple encrypted parts and stored in separate VeKey devices to avoid misappropriation and reduce the possibility of economic loss caused by SPOF.


Email [bd@vechain.com](mailto:bd@vechain.com) if you are interested in, introduce your business and why you are interested in the VeKey solution.