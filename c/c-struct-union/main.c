#include <stdio.h>
#include <stdint.h>

struct Hello {
	uint8_t a;
	uint8_t b;
	union {
		uint8_t c;
		uint16_t d;
	};
	union {
		struct {
			uint8_t e;
			uint8_t f;
		};
		struct {
			uint16_t g;
		};
	};
};

int main()
{
	struct Hello instance;
	instance.a = 0xAB;
	instance.b = 0xCD;
	instance.d = 0xBEEF;
	instance.e = 0xAD;
	instance.f = 0xDE;

	printf("%#2.2X %#2.2X %#4.4X %#4.4X\n", instance.a, instance.b, instance.c, instance.g);
	return 0;
}
