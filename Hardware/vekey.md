# VeKey Manual
The VeKey is used as a digital signature along with your own private key
- The VeKEY does not operate with a battery, you can use a standard micro USB cable to connect it to a PC to give it power in order to execute the transaction signature.
- The OLED display screen is mono white in color on a plain black background.
- There are three menu keys to operate the device.
- There is a fingerprint module for more secure authentication.
- No dedicated power on-off key, you can use USB cable to power on/off VeKEY.



## First time to set PIN code

When you receive your VeKey and turn it on for the first time, you need to set a new PIN code.
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/fbf38ef-VeKey_-2.png",
        "VeKey -2.png",
        216,
        333,
        "#8e8157"
      ]
    }
  ]
}
[/block]
Enter OK to begin setting up a new PIN code.
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/8e54f27-VeKey_-3.png",
        "VeKey -3.png",
        737,
        200,
        "#e9e9e9"
      ]
    }
  ]
}
[/block]
- PIN code must be no more than 6 digits.
- Press the left menu key to lower the number from “5”. Press the right menu key for increase the number from “5”.
- Press the middle menu key to confirm the number you would like and move on to the next.
- The new PIN code must be inputted twice to confirm, and they must match for it to be successful.
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/ffa6be0-VeKey_-4.png",
        "VeKey -4.png",
        974,
        485,
        "#908461"
      ]
    }
  ]
}
[/block]
 
## First time to set fingerprint

After setting your PIN code, you must set your fingerprint.
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/43f90f1-VeKey_-5.png",
        "VeKey -5.png",
        974,
        210,
        "#f0f0f1"
      ]
    }
  ]
}
[/block]
-Place your finger on the module to scan your fingerprint according to the system prompt.
-Up to two fingerprints can be collected.

## PIN code verification

It happens in a scenario where PIN code authentication is required.
 
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/d7e60e2-VeKey_-6.png",
        "VeKey -6.png",
        316,
        150,
        "#e7e7e8"
      ]
    }
  ]
}
[/block]
-Input the correct PIN code and press the middle menu key to confirm to move onto the next process. 
-If you input the incorrect PIN code, the system will prompt a “PIN code Error. Please enter again” message. If you input the incorrect password 3 times, the device will force restart. If you input the incorrect password totally for 9 times, the device will be erased forcibly. 

## Fingerprint verification

It happens in a scenario where Fingerprint authentication is required.
 
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/94b38c6-VeKey_-7.png",
        "VeKey -7.png",
        293,
        143,
        "#e6e6e6"
      ]
    }
  ]
}
[/block]
-Press your fingerprint. If the fingerprint matches, enter the next process.
-If the fingerprint does not match, system will remind “Fingerprint Error. Please try again”. If the fingerprint does not match for 3 times, the device will force restart. If fingerprint does not match for a total of 9 times, the device will automatically erase itself.

##Generate New Private key and address

After setting the new PIN code and fingerprint, you can generate your private key and get your address.
 
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/e1c5d36-VeKey_-8.png",
        "VeKey -8.png",
        575,
        422,
        "#89805d"
      ]
    }
  ]
}
[/block]
-Enter new and proceed.
-Write down the 12 mnemonic phrase in sequence.
-Press the left menu key and the right menu key to navigate between words.
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/0052da0-VeKey_-9.png",
        "VeKey -9.png",
        597,
        395,
        "#8e865c"
      ]
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/2128b66-VeKey_-10.png",
        "VeKey -10.png",
        974,
        402,
        "#9e9671"
      ]
    }
  ]
}
[/block]
 -When you have written down all 12 mnemonic phrases, the system will remind you to confirm whether you have done so. Press the left menu key to revise and check the phrases you have entered or press the right menu key to go to confirm your mnemonic phrases.
-Double confirm your mnemonics: The system will randomly select one mnemonic in a certain sequence and 12 random words for selection, press the left menu key and right menu key to view all words. Select the correct word among the 12 words by pressing the middle key. You should correctly confirm 3 of the random words to retrieve your raw address. Press the right key and a “Congratulations” page will display and then show you the main menu.
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/52630d9-VeKey_-11.png",
        "VeKey -11.png",
        421,
        100,
        "#ededed"
      ]
    }
  ]
}
[/block]
   
-If the mnemonic phrase you select is incorrect, the screen will prompt “Word Error. Picked the wrong word. Please try again.” and require you reselect and submit the correct phrases. If you select the incorrect word for 3 times, the system will remind with "WORD ERROR. Please check and write down all words again” and turns back to the mnemonic page.

## Daily starting up
When you have successfully set the correct PIN code and Fingerprint, you should input PIN code and press fingerprint when daily start up the device. The default verification setting for starting up is double authentication, you can change the setting in “Verification Menu” to select other authentication ways.

## Main menu

## Signature
 
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/7697944-VeKey_-12.png",
        "VeKey -12.png",
        931,
        343,
        "#9a8b67"
      ]
    }
  ]
}
[/block]
-The first menu is “Signature”, you can view other menus with the left/right menu key.
-Press middle menu key to go to signature mode, input correct PIN code and press fingerprint to complete authentication to go to signature.
-Press left menu key to quit signature mode and go back to main menu.
-The default verification setting for signature is double authentication, you can change the setting in “Verification Menu” to select other authentication ways.

##PIN Setting
 
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/f31e3ca-VeKey_-13.png",
        "VeKey -13.png",
        943,
        245,
        "#aa9b7a"
      ]
    }
  ]
}
[/block]
-The second menu is “PIN Setting.”
-Press middle menu key to go to change your PIN code.
-Input correct PIN code and press fingerprint to complete authentication to start setting a new PIN code.
-Input the new PIN code twice and you will automatically be brought to the main menu.
-PIN setting requires compulsory double authentication

##Fingerprint
 
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/df2c426-VeKey_-14.png",
        "VeKey -14.png",
        868,
        331,
        "#9b8967"
      ]
    }
  ]
}
[/block]
-The third menu is “Fingerprint”
-Press middle menu key to go to change Fingerprint
-Input correct PIN code and press fingerprint to complete authentication to start setting s new Fingerprint.
-Move your finger to collect the fingerprint according to the systems instructions and automatically go to the main menu.
-Fingerprint mode requires compulsory double authentication

##Verification
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/095eb37-VeKey_-15.png",
        "VeKey -15.png",
        970,
        306,
        "#a29570"
      ]
    }
  ]
}
[/block]
 
-The fourth menu is “Verification”.
-Press the middle menu key to go to verification mode.
-Input the correct PIN code and press fingerprint to complete authentication and set the verification way for the function “startup” and “Signature”.
-Press left menu key to go back to main menu, press right menu key to select the function you would like to set.
-When set the verification way for the function “startup”, you can choose only PIN code, or only Fingerprint instead of the default double authentication by press the left/right menu key.
-When setting the verification way for the function “signature”, you can choose only PIN code, or only Fingerprint instead of the default double authentication by press the left/right menu key. Besides, you also need to set time interval for authentication. The default setting will “always require” authentication, you can also choose require authentication after 15mins, or 60mins or 4 hours by press the left/right menu key.
-Press middle menu key to confirm your selection.

## About
 
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/694e94a-VeKey_-16.png",
        "VeKey -16.png",
        974,
        162,
        "#f3f3f5"
      ]
    }
  ]
}
[/block]
-The fifth menu is “About”
-Press middle menu key to view detailed information of the device, including Device ID, Firmware Version, Raw Address. Press the left menu key to go back to main menu, and press the right menu key to view the 3 detailed information.

##Erase
 
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/c4ef3ea-VeKey_-17.png",
        "VeKey -17.png",
        974,
        245,
        "#bbb49d"
      ]
    }
  ]
}
[/block]
-The sixth menu is “ERASE” which could entirely erase device as a totally new one.
-Press middle menu key to enter. Then press left menu key to quit erase, or press right menu key to confirm erase. 
-Input PIN code and press fingerprint to complete authentication and start erasing
-After two seconds, erase operation will be done and press OK to reboot.

##Recovery

-You could recover your old private key in the new device by 12 mnemonics.
[block:image]
{
  "images": [
    {
      "image": [
        "https://doc.vechainworld.io/images/41940a5-VeKey_-18.png",
        "VeKey -18.png",
        974,
        202,
        "#aca38a"
      ]
    }
  ]
}
[/block]
 
-Press right menu key to enter. 
-Input you mnemonics: Press left or right menu key to select the letter of words, and confirm the word after first 3 letters input;
-Double confirm your mnemonics : After complete all 12 mnemonics  input, double review all the words and confirm all of words by pressing center menu key “ok”.
-Confirm the address, and get the Congratulation.