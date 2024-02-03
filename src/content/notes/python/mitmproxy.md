# mitmproxy

## install

```shell
pip install mitmproxy

# Mac
open ~/.mitmproxy/
安装 mitmproxy-ca.pem
设置信任该证书

# open mitm.it after set proxy
mitmproxy --http2 --listen-host 0.0.0.0 --listen-port 8888 -s mitm_test.py
```

## API

```python
# http.HTTPFlow 实例 flow
flow.request.headers #获取所有头信息，包含Host、User-Agent、Content-type等字段
flow.request.url #完整的请求地址，包含域名及请求参数，但是不包含放在body里面的请求参数
flow.request.pretty_url #同flow.request.url目前没看出什么差别
flow.request.host #域名
flow.request.method #请求方式。POST、GET等
flow.request.scheme #什么请求 ，如https
flow.request.path # 请求的路径，url除域名之外的内容
flow.request.get_text() #请求中body内容，有一些http会把请求参数放在body里面，那么可通过此方法获取，返回字典类型
flow.request.query #返回MultiDictView类型的数据，url直接带的键值参数
flow.request.get_content()#bytes,结果如flow.request.get_text()
flow.request.raw_content #bytes,结果如flow.request.get_content()
flow.request.urlencoded_form #MultiDictView，content-type：application/x-www-form-urlencoded时的请求参数，不包含url直接带的键值参数
flow.request.multipart_form #MultiDictView，content-type：multipart/form-data
时的请求参数，不包含url直接带的键值参数

以上均为获取request信息的一些常用方法，对于response，同理
flow.response.status_code #状态码
flow.response.text#返回内容，已解码
flow.response.content #返回内容，二进制
flow.response.setText()#修改返回内容，不需要转码
```

## example.py

```python
# example
def response(flow):
    if "some url" in flow.request.url:
        print("[*] Request: {}".format(flow.request.url))
        print("[*] Response: {}".format(flow.response.text))
```

# charles

```go
package main

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"math/rand"
	"time"
)

const (
	rounds    = 12
	roundKeys = 2 * (rounds + 1)
)

func main() {
	rand.Seed(time.Now().UnixNano())

	name := "mac"

	fmt.Println("name:", name, "    key:", crack(name))
}

func crack(text string) string {

	name := []byte(text)
	length := len(name) + 4
	padded := ((-length) & (8 - 1)) + length
	bs := make([]byte, 4)
	binary.BigEndian.PutUint32(bs, uint32(len(name)))
	buff := bytes.Buffer{}
	buff.Write(bs)
	buff.Write(name)

	var ckName int64 = 0x7a21c951691cd470
	var ckKey int64 = -5408575981733630035
	ck := newCkCipher(ckName)
	outBuff := bytes.Buffer{}

	for i := 0; i < padded; i += 8 {
		bf := buff.Bytes()[i : i+8]
		buf := bytes.NewBuffer(bf)
		var nowVar int64
		if err := binary.Read(buf, binary.BigEndian, &nowVar); err != nil {
			panic(err)
		}

		dd := ck.encrypt(nowVar)

		outBuff.WriteByte(byte(dd >> 56))
		outBuff.WriteByte(byte(dd >> 48))
		outBuff.WriteByte(byte(dd >> 40))
		outBuff.WriteByte(byte(dd >> 32))
		outBuff.WriteByte(byte(dd >> 24))
		outBuff.WriteByte(byte(dd >> 16))
		outBuff.WriteByte(byte(dd >> 8))
		outBuff.WriteByte(byte(dd))

	}
	var n int32
	for _, b := range outBuff.Bytes() {
		n = rotateLeft(n^int32(int8(b)), 0x3)
	}
	prefix := n ^ 0x54882f8a
	suffix := rand.Int31()
	in := int64(prefix) << 32
	s := int64(suffix)
	switch suffix >> 16 {
	case 0x0401:
	case 0x0402:
	case 0x0403:
		in |= s
		break
	default:
		in |= 0x01000000 | (s & 0xffffff)
		break
	}

	out := newCkCipher(ckKey).decrypt(in)

	var n2 int64
	for i := 56; i >= 0; i -= 8 {
		n2 ^= int64((uint64(in) >> i) & 0xff)
	}

	vv := int32(n2 & 0xff)
	if vv < 0 {
		vv = -vv
	}
	return fmt.Sprintf("%02x%016x", vv, uint64(out))
}

type ckCipher struct {
	rk [roundKeys]int32
}

func newCkCipher(ckKey int64) ckCipher {
	ck := ckCipher{}

	var ld [2]int32
	ld[0] = int32(ckKey)
	ld[1] = int32(uint64(ckKey) >> 32)

	ck.rk[0] = -1209970333
	for i := 1; i < roundKeys; i++ {
		ck.rk[i] = ck.rk[i-1] + -1640531527
	}
	var a, b int32
	var i, j int

	for k := 0; k < 3*roundKeys; k++ {
		ck.rk[i] = rotateLeft(ck.rk[i]+(a+b), 3)
		a = ck.rk[i]
		ld[j] = rotateLeft(ld[j]+(a+b), a+b)
		b = ld[j]
		i = (i + 1) % roundKeys
		j = (j + 1) % 2
	}
	return ck
}

func (ck ckCipher) encrypt(in int64) int64 {
	a := int32(in) + ck.rk[0]
	b := int32(uint64(in)>>32) + ck.rk[1]
	for r := 1; r <= rounds; r++ {
		a = rotateLeft(a^b, b) + ck.rk[2*r]
		b = rotateLeft(b^a, a) + ck.rk[2*r+1]
	}
	return pkLong(a, b)
}

func (ck ckCipher) decrypt(in int64) int64 {
	a := int32(in)
	b := int32(uint64(in) >> 32)
	for i := rounds; i > 0; i-- {
		b = rotateRight(b-ck.rk[2*i+1], a) ^ a
		a = rotateRight(a-ck.rk[2*i], b) ^ b
	}
	b -= ck.rk[1]
	a -= ck.rk[0]
	return pkLong(a, b)
}

func rotateLeft(x int32, y int32) int32 {
	return int32(x<<(y&(32-1))) | int32(uint32(x)>>(32-(y&(32-1))))
}

func rotateRight(x int32, y int32) int32 {
	return int32(uint32(x)>>(y&(32-1))) | int32(x<<(32-(y&(32-1))))
}

func pkLong(a int32, b int32) int64 {
	return (int64(a) & 0xffffffff) | (int64(b) << 32)
}
```
