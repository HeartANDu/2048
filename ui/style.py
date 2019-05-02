TEXT_COLORS = {
    'dark': '#776e65',
    'light': '#f9f6f2'
}
BLOCK_COLORS = {
    0: 'background-color: #ccc0b4;',
    2: 'background-color: #eee4da;',
    4: 'background-color: #ece0c8;',
    8: 'background-color: #f2b179;',
    16: 'background-color: #ec8d53;',
    32: 'background-color: #f57c5f;',
    64: 'background-color: #e95937;',
    128: 'background-color: #edcf72;',
    256: 'background-color: #edcc61;',
    512: 'background-color: #edc850;',
    1024: 'background-color: #edc53f;',
    2048: 'background-color: #edc22e;',
    'big': 'background-color: #3e3933;',
}
ADDITIONAL_BLOCK_STYLES = 'font-size: 28pt; font-weight: bold; ' \
                          'border-radius: 5px;'
MAIN_BACKGROUND_COLOR = 'rgb(187, 173, 160)'


def get_block_style(value: int) -> str:
    bg_key = value if value < 2048 else 'big'
    text_key = 'dark' if value < 8 else 'light'
    return '%s color: %s; %s' % (BLOCK_COLORS[bg_key], TEXT_COLORS[text_key],
                                 ADDITIONAL_BLOCK_STYLES)
