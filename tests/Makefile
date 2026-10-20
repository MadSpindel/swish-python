.PHONY: certs download unzip clean

certs: cert.pem key.pem swish.pem

# Download and filenames from:
# https://developer.swish.nu/documentation/environments
#
# Adjust when necessary. MERCHANT is also the merchant number in test_client.py.

URL=https://assets.ctfassets.net/4dca8u8ebqnn/4CgQJUfc6ncjKHooAkqvDx/d27012ce097a5b0f6b151a8ccdfe285d
BASENAME=MSS_test
VERSION=3.0
MERCHANT=1234679304
DIR=client_cert

download:
	wget -c $(URL)/$(BASENAME)_$(VERSION).zip
	@# in case old versions have been downloaded previously, remove them
	find . ! -name '$(BASENAME)_$(VERSION).zip' -name '$(BASENAME)_*.zip' -delete

unzip: download
	unzip -o $(BASENAME)_$(VERSION).zip

cert.pem: unzip
	cp $(DIR)/Swish_Merchant_TestCertificate_$(MERCHANT).pem cert.pem

key.pem: unzip
	cp $(DIR)/Swish_Merchant_TestCertificate_$(MERCHANT).key key.pem

swish.pem: unzip
	cp $(DIR)/Swish_TLS_RootCA.pem swish.pem

clean:
	rm -rf *.pem $(DIR) $(BASENAME)_*.zip
