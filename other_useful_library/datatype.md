# datatype
## bitstring
[官网](https://github.com/scott-griffiths/bitstring)
把二进制转化成01
```python
from bitstring import BitArray
BitArray(b"123").bin  # '001100010011001000110011'

BitArray(HexBytes("0x7f")).int  # 127   01111111
BitArray(HexBytes("0x80")).int  # -128  10000000
```

## base58
base58是bytes转化到bytes
```
import base58
base58.b58encode(b'123')  # b'HXRC'
base58.b58decode(b'HXRC')  # b'123'
```

## base64

## [hexbytes](https://hexbytes.readthedocs.io/en/stable/)
处理字符串和十六进制
```python
from hexbytes import HexBytes
HexBytes(b"123")  // HexBytes("0x313233")
HexBytes(b"123").hex()  // "0x0123"

HexBytes("123")  // HexBytes("0x0123")
HexBytes("123").hex()  // "0x313233"
```
* len  2个hex为1个长度
* slice `HexBytes("0xffff")[0:1] == HexBytes("0xff")`
* getitem `HexBytes("0xffff")[0] == 255`
