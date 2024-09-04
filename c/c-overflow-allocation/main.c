#include <stdint.h>
#include <stdio.h>
#include <malloc.h>
#include <string.h>

struct pdu {
	uint8_t len_buf;
	uint8_t buf[0];		/* Zero size */
};

struct pdu *new_pdu(uint8_t len)
{
	int size = sizeof(struct pdu) + len;
	return (struct pdu *)malloc(size);
}

void init_pdu(struct pdu *pdu, char *text, int len)
{
	pdu->len_buf = len;
	memcpy(pdu->buf, text, len);
}

int main(void)
{
	char text[] = "Hello World";
	int len = sizeof(text);
	struct pdu *pdu;

	pdu = new_pdu(len);
	init_pdu(pdu, text, len);

	printf("sizeof(struct pdu): %u\n", (unsigned int)sizeof(struct pdu));
	printf("%s: len(%d), third index(%c)\n", pdu->buf, pdu->len_buf,
							pdu->buf[2]);

	free(pdu);

	return 0;
}
