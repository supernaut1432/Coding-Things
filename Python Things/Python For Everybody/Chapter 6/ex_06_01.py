text = "X-DSPAM-Confidence:    0.8475"
cpos = text.find(':')
# print(cpos)
ntex = text[cpos+1:]
# print(ntex)
num = float(ntex)
print(num)
