import boto3
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

# With no parameters or configuration, boto3 will look for
# access keys in these places:
#
#    1. Environment variables (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY)
#    2. Credentials file (~/.aws/credentials or
#         C:\Users\USER_NAME\.aws\credentials)
#    3. AWS IAM role for Amazon EC2 instance
#       (http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)
# 
# More here: #https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html
# 

polly = boto3.Session(profile_name="default").client("polly");

file_name = os.path.splitext(str(sys.argv[1]))[0]
script_name = "%s.txt" % file_name
audio_name = "%s.mp3" % file_name

print(file_name)

output = os.path.join(audio_name)
file = open(output, "wb")

with open(script_name, 'r') as f:
	data = f.read().replace('\n', '')

d = data.split("{")

for sp in d:
	components = sp.split("}")
	if len(components) <= 1:
		continue
	else:
		voice = components[0]
		text = components[1]

		# replace pauses with ssml format
		text = text.replace('--s--', '<break time="50ms"/>')
		text = text.replace('--m--', '<break time="200ms"/>')
		text = text.replace('--l--', '<break time="500ms"/>')

		ssml = '<speak><p><amazon:domain name="conversational">%s</amazon:domain></p><break time="500ms"/></speak>' % (text)
		print(voice)
		print(ssml)

		try:
			# Request speech synthesis
			response = polly.synthesize_speech(TextType="ssml",Engine="neural", Text=ssml, OutputFormat="mp3", VoiceId=voice)
		except (BotoCoreError, ClientError) as error:
			# The service returned an error, exit gracefully
			print(error)
			sys.exit(-1)

		# Access the audio stream from the response
		if "AudioStream" in response:
			# Close the stream
			with closing(response["AudioStream"]) as stream:
				
				try:
					# write to file
					file.write(stream.read())
				except IOError as error:
					# Could not write to file, exit gracefully
					print(error)
					sys.exit(-1)

		else:
			# The response didn't contain audio data, exit gracefully
			print("Could not stream audio")
			sys.exit(-1)


