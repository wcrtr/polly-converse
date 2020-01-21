# polly-converse
A simple python script that creates an audio conversation from a script using Amazon Polly.

## Create a script

1. Create a plain text file for your conversation
2. Use curly braces to designate [voices]https://docs.aws.amazon.com/polly/latest/dg/voicelist.html (Voice names are case sensitive)
3. Use --s--, --m--, --l-- flags in your script to quickly add short, medium, or long pauses.
4. You can use your own [SSML](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html) tags in the script for more controls.

## Example Script

```
{Matthew}
Hey there. Hello.
{Joanna}
Hello!
{Matthew}
How's life?
{Joanna}
It's ok!
{Matthew}
Great to hear.
{Joanna}
```

## Running

* You must install the boto3 python library:

`pip install boto3 --user`

* And enable the [Polly](https://console.aws.amazon.com/polly/home/SynthesizeSpeech) service from your [AWS console](https://console.aws.amazon.com)

* [set up your AWS credentials](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html)

* Write your script and run `python polly.py your-script.txt`

The script outputs an mp3 file with the same name as your script.

## Learn more

* [List of Polly Voices]https://docs.aws.amazon.com/polly/latest/dg/voicelist.html
* [Supported SSML Tags](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html)
* [Polly Documentation](https://docs.aws.amazon.com/polly/latest/dg/what-is.html)

