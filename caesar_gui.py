import PySimpleGUI as sg

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalnum():
            if char.isalpha():
                shifted = ord(char) + shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
                result += chr(shifted)
            elif char.isdigit():
                shifted = ord(char) + shift
                if shifted > ord('9'):
                    shifted -= 10
                elif shifted < ord('0'):
                    shifted += 10
                result += chr(shifted)
        else:
            result += char
    return result

sg.theme('LightGrey1')

layout = [
    [sg.Text('Caesar Cipher Tool', size=(30, 1), font=('Helvetica', 20))],
    [sg.Text('Select Operation:'), sg.Radio('Encrypt', 'RADIO1', default=True, key='-ENCRYPT-', enable_events=True),
     sg.Radio('Decrypt', 'RADIO1', key='-DECRYPT-', enable_events=True)],
    [sg.Text('Text to Encrypt/Decrypt:'), sg.InputText(key='-TEXT-')],
    [sg.Text('Shift (0-25):'), sg.Slider(range=(0, 25), orientation='h', size=(20, 15), default_value=3, key='-SHIFT-')],
    [sg.Button('Process'), sg.Button('Clear'), sg.Button('Exit')],
    [sg.Multiline('', size=(60, 10), key='-OUTPUT-')]
]

window = sg.Window('Caesar Cipher Tool', layout, resizable=False, icon='caesar.ico')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        window['-TEXT-'].update('')
        window['-OUTPUT-'].update('')
    if event == 'Process':
        text = values['-TEXT-']
        shift = int(values['-SHIFT-'])
        try:
            if values['-ENCRYPT-']:
                result = caesar_cipher(text, shift)
                info = f"[ Characters shifted: +{shift} ]"
            elif values['-DECRYPT-']:
                result = caesar_cipher(text, -shift)
                info = f"[ Characters shifted: -{shift}  ]"
            window['-OUTPUT-'].print(info + ' Result : ' + result)
        except Exception as e:
            sg.popup_error(f"An error occurred: {e}")

window.close()
