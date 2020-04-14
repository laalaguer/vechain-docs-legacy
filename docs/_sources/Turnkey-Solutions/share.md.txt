# VeKey based Threshold Signature Turnkey Solution

[block:api-header]
{
  "title": "What is VeKey based Threshold Signature？"
}
[/block]
With the continuous development of blockchain, further adoption of the technology is expected, leading to an increase in business investment in digital assets. To prepare for this, enterprises need to be more efficient and proficient in managing their own digital assets. Blockchain, after all, has ushered in incredible transparency and audibility. Enterprises also need to be aware of the risks associated, especially SPOF (single point of failure). We feel it is imperative to have an advanced solution which could be implemented in a way that aligns with enterprises' risk management and internal control policies 

At present, there are two common solutions for enterprises to manage cryptocurrencies or tokenized assets:

1. Cold wallet (such as hardware wallet), which is not suitable for enterprises because there is a single point of risk 

2. Third-party asset custody service, which is managed by enterprises, custodians, or third-party using multiple signatures. This solution relies on the strength of internal control and security measures of the third party

VeChain's turnkey solution for enterprises to manage their own crypto assets is a threshold based off-chain multi-signature solution using a modified [Shamir's Secret Sharing](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing) to avoid the SPOF and third-party risks. 
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/0af2587-Screen_Shot_2019-04-22_at_15.24.51.png",
        "Screen Shot 2019-04-22 at 15.24.51.png",
        698,
        380,
        "#171614"
      ]
    }
  ]
}
[/block]
Designed for VeChain ecosystem members and the developers focused on providing secure private key management services, VeKey Based Threshold Signature Turnkey Solution combines secure hardware and software in one single Solution in an effort to support enterprises’ management of digital assets. 
[block:api-header]
{
  "title": "Features"
}
[/block]
VeKey Based Threshold Signature Turnkey Solution is an easy-to-use, certified Solution for the secure storage of private keys and the management of digital signatures and identities. For the purpose of increasing its security and availability, VeChain designed VeKey, a security identity hardware, for the Solution, it features multiple complementary security layers, including:
* Compulsory double authentication (biometric identification via fingerprint + PIN)
* Software-based security mechanism
* Back-end verification
* Hardware Secure Element

To provide the highest level of security and the best Solution on the market, VeChain equipped VeKey with CG4Q series chips developed by Datang Microelectronics, a holding subsidiary of public listed company Datang Telecom Technology Co., Ltd. The chips are constructed integrating independent secure coprocessor and multiple chip security technologies to ensure a shielded operating and storage environment for confidential data. Featuring hardware-based encryption, memory access control unit, attacks detection, random number generator, and SPA/DPA anti-attack, CG4Q series chips provide robust bank-level security protection and superb performance sufficient to meet the enterprise clients’ demands of security.

With the above-mentioned hardware and software-based security measures in place, this Solution ensures the security of the private keys and enable secure identification of the private key holders.

Through the Solution, private keys can be broken down into multiple encrypted parts and stored in separate VeKey devices. Enterprise users can predefine the number of VeKeys needed to recover the private key. In this way, no single VeKey holder will have absolute control over the assets, thus avoiding misappropriation.

The solution can also be used to avoid economic damages caused by the loss of private keys, as it can always be recovered so long as the enterprise can provide the predefined number of VeKeys.

More importantly, the Solution supports asynchronous operation, with which the VeKey holders are enabled to review the transaction applications from anywhere, at any time. In the event any VeKey holder wants to initiate a transaction, they would need only to log into the system and submit an application for review, the transaction will be signed and broadcasted to the blockchain when it is approved by the predefined number of VeKey holders. With this process, a remote threshold multi-signature can be achieved, thus increasing transaction efficiency and security.
[block:api-header]
{
  "title": "Specific Functions"
}
[/block]
  * Users can register, log in, create projects and set project parameters such as threshold in the web portal
  * Any VeKey holder in the project can initiate transactions for other VeKey holders' approval
  * Project users can audit the transaction history
  * In this solution, the core private key is scattered in secret shares that are stored in multiple Vekey devices. Only when the number of approvers meets the threshold requirement the core private key is restored. No single user can recover the core private key which controls the asset
  * The private key is recovered in the VeKey device or HSM
  * The total number of asset management personnel and threshold signature can be set according to actual business needs
  * The backend system monitors the pending transactions and signature status
[block:api-header]
{
  "title": "Use Cases"
}
[/block]
This turnkey solution can be used to further develop into a secure multi-signature wallet product which can be run as a SaaS product to serve both retail and enterprises clients. It can also be integrated by blockchain project teams, startups or enterprises to manage their own cryptocurrencies or tokenized assets. 

If you are interested, please follow [this process](https://doc.vechainworld.io/docs/overview-1#section-im-interested-in-the-turnkey-solution-how-can-i-get-more-information) to learn more information.