#time complexity O(l + r) where l is the len of s and r is the remainder substring length(r = n%l) 
def repeatedString(s, n):
    leng = len(s)
    count = find_a_count(s)
    full_repeats = n // leng
    total_count = count * full_repeats
    remainder = n % leng
    total_count += find_a_count(s[:remainder])
    return total_count

def find_a_count(s:str):
    return s.count('a')

print(repeatedString("epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq", 549382313570))
print(repeatedString("ojowrdcpavatfacuunxycyrmpbkvaxyrsgquwehhurnicgicmrpmgegftjszgvsgqavcrvdtsxlkxjpqtlnkjuyraknwxmnthfpt", 685118368975))