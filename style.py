class Style:
    def __init__(self):
        self.styles = {
            0: 'background-color: #ccc0b4;',
            2: 'background-color: #eee4da; color: #776e65;',
            4: 'background-color: #ece0c8; color: #776e65;',
            8: 'background-color: #f2b179; color: #f9f6f2;',
            16: 'background-color: #ec8d53; color: #f9f6f2;',
            32: 'background-color: #f57c5f; color: #f9f6f2;',
            64: 'background-color: #e95937; color: #f9f6f2;',
            128: 'background-color: #edcf72; color: #f9f6f2;',
            256: 'background-color: #edcc61; color: #f9f6f2;',
            512: 'background-color: #edc850; color: #f9f6f2;',
            1024: 'background-color: #edc53f; color: #f9f6f2;',
            2048: 'background-color: #edc22e; color: #f9f6f2;',
            'big': 'background-color: #3e3933; color: #f9f6f2;',
        }
        self.additional = 'font-size: 28pt; font-weight: bold;'

    def get_style(self, value: int):
        key = value
        if key > 2048:
            key = 'big'
        return '%s %s' % (self.styles[key], self.additional)


style = Style()
