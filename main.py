s = "agpygmqgxyxfiuimypmvcmssvuiyjcggxripiuxyjrlkwdivxkwtyqxtexhmquxejdjtswxfikrdiprgxdlcgqpyvmjcrsqypumcfwrqqoelwcqkxritspgfepgomrhgtorbwqrwelcesxwghgvkxgspwlyrmpxrikelsbmrcqjmeqiuxorbwvszvmxggdxficrsqyphvyqbepkovzctixhcvkrqmrpgwcgmrutsgsswwziplctcmrqccliqekhdlyxkjmsjstmxkgwoesrjcrvyxcgvmfirlgvosskjxdszidydjcadvskfxncmsjstinelmoevwrlgvoepijsgititryxyjgameqiumxafmelfmtmfgypmvuebirlgqcijzgwzvmxggdmtivloogrijswfitmdwcphxrsskjwyfpmildpwgqpyvchkwlclsoikrqicwixmwgidlcfnyolyvosxmxiuasxfxjigeritexhrlgfsvbeumdhyvvwkpmrixriqxtikqjsqocejqqwdpgogeppywjspwsrnmqlrhgwovrepmwejwcvokcrgvkpjcvlogmpqvyjrlghowcvvxryqjqvsrqxcrmirlgpsslxjikrrinsziyrfxriumnhnslogckvcenpcelhesvspifmxhcifwkcqgcryrrvkwdvyqkrdlchgwovrajibilikxripxtiowzvwwramsfryvczgrerbynedmmrqjdlcwwvpeaicjpsphvlowjmildiqxrvyxcgvmyrrskxcjmiuewsbmhmmermqryjasnsbeqwkqspyxghdsrlcxyjrlgwevpswrnmlkeserrvamcezwqpexcparogcwuebcfipgoagxjsexcbeizxgspxristribtjyoeqimjgzovwfkvnelhcpcsrlgjevmjcpvxfiuqkpjitqkqkenwkrbxjicogrqjkpjxjicryogwkrbpkdkvbwkwyjmrgyxmdstqcelhesvspxjixivxrssrrmuxriasnsbsdxjiwerytimerittspjetwcskiqjglggjebizvqaxxfmutbszedpiqyogwdlcgcxovnmnpkvczgrwspiesxwnmeyyyqeosxkrlgkbicrnikzcwvlkruswpnsrlgvgmqididlcgcwopcxwwcicxjixafivlovrlglkfgxuspxfikrciaxymvprltsgelcnmqlryrsxxfitmnhjiylkxuswpncmyfssjwswaovcedmqgyxgvzmjpcvglwpkooqmwvsdlcvfipilwgpowqgtikxsvgwissaqyvhdighlclmildelhnmogmreikpchdcnewwqhyxfiuimerittspjetwglcrvloqmvpmxkjmildgmqgwdlccevoinhqaxxfiuxoqmjvlojmsftvelxcrnpgiesxgceninekspkdlcxjmmofitfkkcephnvwwvmmoqephviyzgwxiyvvlokpswrnelhkxswmfxmyyqxjedylhgvcyalembgsquxkraiuxrizvqaxgmpqvbiypncliasoicenvqxogrmqrsxkmildmlhginfcetkeibxjedxfieediptkpvepwjefmlkdimskidvyalgqrmiypghdlcquivzcwqrdlcktserbephdlyxyigipitifipwkrqxfiuxkxcshxrmlkufexrlkwswlsvwyfcgcyciulkpoacqccceweueqilitevvspgxrerpcvqiaevibtgpnebwdighlclmildelhnmogmreikpchdcnewmvmcfwrqqoelwcpgewwvlogywgxrerxjiiepidvyalwqqosdxjiwwrmnpbirekrsrexjiqvcipgypmvyiwewxjixgmrepehcxjedxfijelmrshgyraicpsrexjiwwcpxicfwhccmekihmbwrephdlyxvlofpsyrmsjstmcejevibeberxkxgsp"

# helper method to pretty print an array
def printbuckets(input):
	for dex in range(len(input)):
		print(chr(dex + ord('a')) + ": "+ str(input[dex]))

# helper method to pretty print an array and graph it
def printbucketsgraph(input):
	for dex in range(len(input)):
		''.join(['|' for i in range(input[dex])])
		print(chr(dex + ord('a')) + ": "+ ''.join(['|' for i in range(input[dex])]) + str(input[dex]))


# frequency analysis
# count the number of occurances of each char in s
def bucket(s):
	buckets = [0] * 26 # 26 lower case letters
	for char in s:
		buckets[ord(char) - ord("a")] += 1

	return buckets

# frequency analysis but using chunks
# count the number of occurances of each letter in s considering the key length l
def chunked_bucket(s, l):
	# generate buckets for each letter for each letter in key
	buckets = [[0 for col in range(26)] for row in range(l)] 
	for idx, char in enumerate(s):
		# bucket according to the modulo of the key length
		buckets[idx % l][ord(char) - ord("a")] += 1 

	return buckets

# get the key using the chunked bucket analysis output
def find_key(buckets):
	shift_keys = [0] * 6
	for idx, bucket in enumerate(buckets):
		# get the max index
		max_idx = bucket.index(max(bucket)) 
		# determine the shift amount
		shift_key = max_idx - 4 if max_idx - 4 >= 0 else max_idx + 22 # determine the shift amount
		# store the computed shift for that letter
		shift_keys[idx] = shift_key 
	# return the shift key serialized as a string
	return ''.join([chr(elem + ord('a')) for elem in shift_keys]) 

# given encoded text, decode text using key
def decode(cipherInput, key):
	# generate new list for cipher decode
	cipherIntList = [ord(i) for i in cipherInput]
	
	# generate list for key string
	keyIntList = [ord(dex) for dex in key]
	result = []
	
	for dex in range(len(cipherInput)):
		# shift cipher text by key
		value = (cipherIntList[dex] - keyIntList[dex % len(key)]) % 26
		result += chr(value + ord('a')) # append to result
	# return result serialized as string
	return ''.join(result)

def main():
	
	print("------------frequency analyis---------------")
	b= bucket(s)
	printbuckets(b)
	
	# printbucketsgraph(b)
	print("------------frequency analyis---------------")
	
	print("------------chunked frequency analyis---------------")
	buckets = chunked_bucket(s,6)
	print(buckets)
	# pretty print first chunk
	printbucketsgraph(buckets[0])
	# todo: uncomment if you want to pretty print all buckets
	# for buck in buckets:
	# 	printbuckets(buck)
	# 	print("----")
	print("------------chunked frequency analyis---------------")
	
	# print("------------maxxes---------------")
	# maxs = list(map(lambda x: [x.index(max(x)), max(x)], buckets))
	# print(maxs)
	# print("------------maxxes---------------")
	
	print("------------findkey---------------")
	key = find_key(buckets)
	print(key)
	print("------------findkey---------------")

	print("------------decode---------------")
	decoded = decode(s, key)
	print(decoded)
	print("------------decode---------------")

if __name__=="__main__":
	main()
