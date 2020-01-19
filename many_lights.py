from apa102_pi.driver import apa102

strip = apa102.APA102(num_led=1, order='rgb')

strip.clear_strip()

strip.set_pixel_rgb(1,  0xFF0000)  # Red

strip.show()

strip.cleanup()