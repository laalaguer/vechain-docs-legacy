# HSM based Key Escrow Turnkey Solution

Blockchain technology has been adopted by numerous industries and is set to become a bigger influence over almost every aspect of our lives. From clothing to food to housing to transportation, the applications for blockchain seem limitless. However, that doesn’t mean the process is seamless or that development doesn’t have challenges. One of those is the complicated addresses and complex mnemonic phrases, which are difficult for users to memorize and manage. Thus, users need a practical solution to enable users to best manage and access digital assets, turning to private key escrow services

There are existing solutions as the market for third-party private key escrow services is emerging. These solutions do answer part of the problem — they reduce the intricacies related to access. This increased usage and scaling of transactions expanding also presents an overwhelming pressure for providers regarding costs.

These existing systems fall short on security as well. Consider that those solutions only use software protection and store private keys in the form of digital files. Each transaction needs to call the file stored in the server to complete the decryption and signature transaction on a traditional server. This system is exposed to tampering, as it only holds low-level security barriers.

Enterprises need a solution that solves the shortcomings of existing private key escrow services. Through heavy investments in R&D, VeChain has conceived a unique solution with an HSM based key escrow service. The new product officially launched at the 2019 VeChain Summit held at the Fort Mason’s Festival Pavilion in San Francisco on April 18, 2019.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f286631-6.png",
        "6.png",
        800,
        451,
        "#262525"
      ]
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "What is a Hardware Security Module (HSM)?"
}
[/block]
A hardware security module (HSM) is a dedicated cryptoprocessor that is specifically designed for the protection of the crypto key lifecycle. Hardware security modules act as trust anchors that protect the cryptographic infrastructure of some of the most security-conscious organizations in the world by securely managing, processing, and storing cryptographic keys inside a hardened, tamper-resistant device.

HSM based key escrow turnkey solution, developed based on the hardware products from the world-leading HSM manufacturer [Gemalto](https://www.gemalto.com/), incorporates VeChain Firmware with blockchain features. Suitable for blockchain applications, HSM based key escrow turnkey solution boasts a superior secure storage capability to prevent information leaks.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0e75e68-hsm.jpg",
        "hsm.jpg",
        746,
        174,
        "#b0afac"
      ]
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "More about VeChain's HSM based key escrow turnkey solution secure"
}
[/block]
Enterprises use hardware security modules to protect transactions, identities, and applications, as HSMs excel at securing cryptographic keys and provisioning encryption, decryption, authentication, and digital signing services for a wide range of applications.VeChain HSM based key escrow turnkey solution consists of three parts. HSM, host service, management policy.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c59c89f-image2019-3-12_16-35-46.png",
        "image2019-3-12_16-35-46.png",
        1068,
        294,
        "#e8e8e8"
      ]
    }
  ]
}
[/block]
1. Host:
  *  Host is managing the session with HSM
  *  Host can have HA strategy for HSM cluster
  *  Host has an interface for IT operating engineer to maintain the HSM
  *  Host gives the commands to HSM to get the signature, public key and etc

2. HSM 
  *  HSM certificate verification
  *  HSM Session management
  *  Key and Slot management
  *  Key derive and signing

3. Mangement portal and Risk management policy 
  *  A portal for admin to manage the host parameter, like a whitelist, etc.
  *  Human is always the weakest link, we also compiled recommended internal control and risk management policies relating to the solution. 
[block:api-header]
{
  "title": "Use Cases"
}
[/block]
This turnkey solution can be integrated by custody service providers, exchanges, trust/funds manage crypto assets. It is also an essential component in blockchain solutions that involve tokenized assets. Enterprises can use this solution to provide key escrow service to their users to significantly enhance the user experience and security.

If you are interested, please follow [this process](https://doc.vechainworld.io/docs/overview-1#section-im-interested-in-the-turnkey-solution-how-can-i-get-more-information) to learn more information.