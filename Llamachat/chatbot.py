<<<<<<< HEAD
=======
#!/usr/bin/env python3

>>>>>>> 8006cbd3e68981dd5a4f08ccc85083b062353f64
import subprocess, sys
try:
    import ollama
except ImportError:
    print('This program requires the Ollama Python package to run')
    print('Would you like to install via Pip? Y/N')
    imp = input('>>> ')
    if imp.startswith('Y') or imp.startswith('y'):
        try:
            subprocess.run(['pip3', 'install', 'ollama'], check=True)
            print('Ollama module installed successfully!')
        except subprocess.CalledProcessError as e:
            print(f'Error installing Ollama package: {e}')
            sys.exit()
    elif imp.startswith('N') or imp.startswith('n'):
        sys.exit()
    else:
        print('please enter a valid choice (Y/N)')


def check_installation():
    try:
        subprocess.Popen(['ollama', 'serve'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print('Ollama service started successfully in the background.')
    except FileNotFoundError:
        print('ERROR: Ollama command not found. Please ensure it is installed and in your PATH.')
        sys.exit()
    except Exception as e:
        print(f'ERROR starting Ollama service: {e}')
        sys.exit()

def choose_model():
    model_choice = None
    while not model_choice:
        print('Welcome! What LLM would you like to use today?')
        print('1 for Llama3\n2 for Llama2 Uncensored\n3 for Gemma\n4 for Code Llama\n5 to Quit')
        choice = input('>>> ')
        if choice == '1':
            model_choice = 'llama3'
        elif choice == '2':
            model_choice = 'llama2-uncensored'
        elif choice == '3':
            model_choice = 'gemma:7b'
        elif choice == '4':
            model_choice = 'codellama'
        elif choice == '5':
            sys.exit()
        else:
            print('Please select a valid choice.')

    return model_choice

def main():
    check_installation()
    model_choice = choose_model()
    while True:
        question = input('\nWhat would you like to know?\n')
        try:
            stream = ollama.chat(
                model=model_choice,
                messages=[{'role': 'user', 'content': question}],
                stream=True,
            )
            for chunk in stream:
                print(chunk['message']['content'], end='', flush=True)
            print()
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            print(f'Error: {e}')
            sys.exit()

if __name__ == '__main__':
    main()

