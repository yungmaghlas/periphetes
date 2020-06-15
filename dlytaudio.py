from pytube import YouTube


link = YouTube("https://youtu.be/tVkc6UF1mzI") #plug url
print(link.title)
stream = link.streams.filter(only_audio=True).first() #audio only may not be available for some videos
print(stream)
stream.download('/Users/jaepark/Documents/MusicFiles') #change download destination as needed
