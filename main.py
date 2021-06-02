s = "agpygmqgxyxfiuimypmvcmssvuiyjcggxripiuxyjrlkwdivxkwtyqxtexhmquxejdjtswxfikrdiprgxdlcgqpyvmjcrsqypumcfwrqqoelwcqkxritspgfepgomrhgtorbwqrwelcesxwghgvkxgspwlyrmpxrikelsbmrcqjmeqiuxorbwvszvmxggdxficrsqyphvyqbepkovzctixhcvkrqmrpgwcgmrutsgsswwziplctcmrqccliqekhdlyxkjmsjstmxkgwoesrjcrvyxcgvmfirlgvosskjxdszidydjcadvskfxncmsjstinelmoevwrlgvoepijsgititryxyjgameqiumxafmelfmtmfgypmvuebirlgqcijzgwzvmxggdmtivloogrijswfitmdwcphxrsskjwyfpmildpwgqpyvchkwlclsoikrqicwixmwgidlcfnyolyvosxmxiuasxfxjigeritexhrlgfsvbeumdhyvvwkpmrixriqxtikqjsqocejqqwdpgogeppywjspwsrnmqlrhgwovrepmwejwcvokcrgvkpjcvlogmpqvyjrlghowcvvxryqjqvsrqxcrmirlgpsslxjikrrinsziyrfxriumnhnslogckvcenpcelhesvspifmxhcifwkcqgcryrrvkwdvyqkrdlchgwovrajibilikxripxtiowzvwwramsfryvczgrerbynedmmrqjdlcwwvpeaicjpsphvlowjmildiqxrvyxcgvmyrrskxcjmiuewsbmhmmermqryjasnsbeqwkqspyxghdsrlcxyjrlgwevpswrnmlkeserrvamcezwqpexcparogcwuebcfipgoagxjsexcbeizxgspxristribtjyoeqimjgzovwfkvnelhcpcsrlgjevmjcpvxfiuqkpjitqkqkenwkrbxjicogrqjkpjxjicryogwkrbpkdkvbwkwyjmrgyxmdstqcelhesvspxjixivxrssrrmuxriasnsbsdxjiwerytimerittspjetwcskiqjglggjebizvqaxxfmutbszedpiqyogwdlcgcxovnmnpkvczgrwspiesxwnmeyyyqeosxkrlgkbicrnikzcwvlkruswpnsrlgvgmqididlcgcwopcxwwcicxjixafivlovrlglkfgxuspxfikrciaxymvprltsgelcnmqlryrsxxfitmnhjiylkxuswpncmyfssjwswaovcedmqgyxgvzmjpcvglwpkooqmwvsdlcvfipilwgpowqgtikxsvgwissaqyvhdighlclmildelhnmogmreikpchdcnewwqhyxfiuimerittspjetwglcrvloqmvpmxkjmildgmqgwdlccevoinhqaxxfiuxoqmjvlojmsftvelxcrnpgiesxgceninekspkdlcxjmmofitfkkcephnvwwvmmoqephviyzgwxiyvvlokpswrnelhkxswmfxmyyqxjedylhgvcyalembgsquxkraiuxrizvqaxgmpqvbiypncliasoicenvqxogrmqrsxkmildmlhginfcetkeibxjedxfieediptkpvepwjefmlkdimskidvyalgqrmiypghdlcquivzcwqrdlcktserbephdlyxyigipitifipwkrqxfiuxkxcshxrmlkufexrlkwswlsvwyfcgcyciulkpoacqccceweueqilitevvspgxrerpcvqiaevibtgpnebwdighlclmildelhnmogmreikpchdcnewmvmcfwrqqoelwcpgewwvlogywgxrerxjiiepidvyalwqqosdxjiwwrmnpbirekrsrexjiqvcipgypmvyiwewxjixgmrepehcxjedxfijelmrshgyraicpsrexjiwwcpxicfwhccmekihmbwrephdlyxvlofpsyrmsjstmcejevibeberxkxgsp"

# todo: replace when not testing
# s="abcdefabcdefabcdef"

def bucket(s):
	buckets = [0] * 26
	for char in s:
		buckets[ord(char) - ord("a")] += 1

	return buckets

def chunked_bucket(s, l):
	buckets = [[0 for col in range(26)] for row in range(l)]
	for idx, char in enumerate(s):
		buckets[idx % l][ord(char) - ord("a")] += 1

	return buckets


def find_key(buckets):
	shift_keys = [0] * 6
	for idx, bucket in enumerate(buckets):
		max_idx = bucket.index(max(bucket))
		shift_key = max_idx - 4 if max_idx - 4 >= 0 else max_idx + 22
		shift_keys[idx] = shift_key
	return ''.join([chr(elem + ord('a')) for elem in shift_keys])

def decode(cipherInput, key):
	keyIntList = [ord(dex) for dex in key]
	cipherIntList = [ord(i) for i in cipherInput]
	result = []
	for dex in range(len(cipherInput)):
		value = (cipherIntList[dex] - keyIntList[dex % len(key)]) % 26
		result += chr(value + ord('a'))
	return ''.join(result)		

def main():
	
	print("------------frequency analyis---------------")
	print(bucket(s))
	print("------------frequency analyis---------------")
	
	print("------------chunked frequency analyis---------------")
	buckets = chunked_bucket(s,6)
	print(buckets)
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
