from pydub import AudioSegment

def mp3_length(input_file, input_format):
	if (input_format == "mp3"):
		recording = AudioSegment.from_mp3(input_file)
	elif (input_format == "wav"):
		recording = AudioSegment.from_wav(input_file)
	elif (input_format == "ogg"):
		recording = AudioSegment.from_ogg(input_file)
	else:
		return -1

	return len(recording)


def mp3_segment(input_file, input_format, output_file, start_time, end_time):
	if (input_format == "mp3"):
		recording = AudioSegment.from_mp3(input_file)
	elif (input_format == "wav"):
		recording = AudioSegment.from_wav(input_file)
	elif (input_format == "ogg"):
		recording = AudioSegment.from_ogg(input_file)
	else:
		return False

	# len() and slicing are in milliseconds
	if (len(recording) < end_time):
		return False

	segment = recording[start_time:end_time]
	segment.export(output_file, format="mp3")

	return True

def mp3_segment_all(input_file, input_format, boundaries, output_file):
	if (input_format == "mp3"):
		recording = AudioSegment.from_mp3(input_file)
	elif (input_format == "wav"):
		recording = AudioSegment.from_wav(input_file)
	elif (input_format == "ogg"):
		recording = AudioSegment.from_ogg(input_file)
	else:
		return False

	for i in range(len(boundaries)):
		start, end = boundaries[i]
		recording[start:end].export("segment/"+output_file+"_"+str(i+1)+".mp3", format="mp3")

	return True