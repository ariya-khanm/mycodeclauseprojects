import time

def calculate_wpm(start_time, end_time, word_count):
    elapsed_time = end_time - start_time
    wpm = (word_count / elapsed_time) * 60
    return wpm

def calculate_accuracy(typed_text, reference_text):
    typed_words = typed_text.split()
    reference_words = reference_text.split()
    correct_words = 0

    for i in range(min(len(typed_words), len(reference_words))):
        if typed_words[i] == reference_words[i]:
            correct_words += 1

    accuracy = (correct_words / len(reference_words)) * 100
    return accuracy

def typing_speed_test():
    reference_text = "In programming, clean code is the key to successfull projects."
    print("Type the following sentence as fast and accurately as you can:")
    print(reference_text)
    input("Press Enter to start...")

    start_time = time.time()
    typed_text = input()
    end_time = time.time()

    word_count = len(reference_text.split())
    wpm = calculate_wpm(start_time, end_time, word_count)
    accuracy = calculate_accuracy(typed_text, reference_text)

    print(f"\nYour typing speed is: {wpm:.2f} words per minute")
    print(f"Your accuracy is: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_speed_test()

