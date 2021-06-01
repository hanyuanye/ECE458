s = "agpygmqgxyxfiuimypmvcmssvuiyjcggxripiuxyjrlkwdivxkwtyqxtexhmquxejdjtswxfikrdiprgxdlcgqpyvmjcrsqypumcfwrqqoelwcqkxritspgfepgomrhgtorbwqrwelcesxwghgvkxgspwlyrmpxrikelsbmrcqjmeqiuxorbwvszvmxggdxficrsqyphvyqbepkovzctixhcvkrqmrpgwcgmrutsgsswwziplctcmrqccliqekhdlyxkjmsjstmxkgwoesrjcrvyxcgvmfirlgvosskjxdszidydjcadvskfxncmsjstinelmoevwrlgvoepijsgititryxyjgameqiumxafmelfmtmfgypmvuebirlgqcijzgwzvmxggdmtivloogrijswfitmdwcphxrsskjwyfpmildpwgqpyvchkwlclsoikrqicwixmwgidlcfnyolyvosxmxiuasxfxjigeritexhrlgfsvbeumdhyvvwkpmrixriqxtikqjsqocejqqwdpgogeppywjspwsrnmqlrhgwovrepmwejwcvokcrgvkpjcvlogmpqvyjrlghowcvvxryqjqvsrqxcrmirlgpsslxjikrrinsziyrfxriumnhnslogckvcenpcelhesvspifmxhcifwkcqgcryrrvkwdvyqkrdlchgwovrajibilikxripxtiowzvwwramsfryvczgrerbynedmmrqjdlcwwvpeaicjpsphvlowjmildiqxrvyxcgvmyrrskxcjmiuewsbmhmmermqryjasnsbeqwkqspyxghdsrlcxyjrlgwevpswrnmlkeserrvamcezwqpexcparogcwuebcfipgoagxjsexcbeizxgspxristribtjyoeqimjgzovwfkvnelhcpcsrlgjevmjcpvxfiuqkpjitqkqkenwkrbxjicogrqjkpjxjicryogwkrbpkdkvbwkwyjmrgyxmdstqcelhesvspxjixivxrssrrmuxriasnsbsdxjiwerytimerittspjetwcskiqjglggjebizvqaxxfmutbszedpiqyogwdlcgcxovnmnpkvczgrwspiesxwnmeyyyqeosxkrlgkbicrnikzcwvlkruswpnsrlgvgmqididlcgcwopcxwwcicxjixafivlovrlglkfgxuspxfikrciaxymvprltsgelcnmqlryrsxxfitmnhjiylkxuswpncmyfssjwswaovcedmqgyxgvzmjpcvglwpkooqmwvsdlcvfipilwgpowqgtikxsvgwissaqyvhdighlclmildelhnmogmreikpchdcnewwqhyxfiuimerittspjetwglcrvloqmvpmxkjmildgmqgwdlccevoinhqaxxfiuxoqmjvlojmsftvelxcrnpgiesxgceninekspkdlcxjmmofitfkkcephnvwwvmmoqephviyzgwxiyvvlokpswrnelhkxswmfxmyyqxjedylhgvcyalembgsquxkraiuxrizvqaxgmpqvbiypncliasoicenvqxogrmqrsxkmildmlhginfcetkeibxjedxfieediptkpvepwjefmlkdimskidvyalgqrmiypghdlcquivzcwqrdlcktserbephdlyxyigipitifipwkrqxfiuxkxcshxrmlkufexrlkwswlsvwyfcgcyciulkpoacqccceweueqilitevvspgxrerpcvqiaevibtgpnebwdighlclmildelhnmogmreikpchdcnewmvmcfwrqqoelwcpgewwvlogywgxrerxjiiepidvyalwqqosdxjiwwrmnpbirekrsrexjiqvcipgypmvyiwewxjixgmrepehcxjedxfijelmrshgyraicpsrexjiwwcpxicfwhccmekihmbwrephdlyxvlofpsyrmsjstmcejevibeberxkxgsp"


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

	return shift_keys

def decode(s, keys):
	length = len(keys)
	decoded = ""
	for idx, char in enumerate(s):
		key = keys[idx%length]
		new_int = ord(char) + key if ord(char) + key <= ord("z") else ord(char) + key - 26
		new_char = chr(new_int)
		decoded += new_char

	return decoded
		

def main():
	buckets = chunked_bucket(s,6)
	print(buckets)
	maxs = list(map(lambda x: [x.index(max(x)), max(x)], buckets))
	print(maxs)
	keys = find_key(buckets)
	print(keys)
	decoded = decode(s, keys)
	print(decoded)

if __name__=="__main__":
	main()
