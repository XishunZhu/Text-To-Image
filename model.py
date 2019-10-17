"""
Model architecture
"""

import utils as u

class Text_GAN(object):
    def __init__(self, max_text_len):
        u.type_assert('max_text_len', max_text_len, int)
        self.max_text_len = max_text_len
