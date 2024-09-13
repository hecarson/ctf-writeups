from pwnlib.tubes.remote import remote

def get_res(guess: str, ans: str) -> int:
    res = 1
    for i in range(5):
        a = ord(guess[i]) - ord('a')
        b = ord(ans[i]) - ord('a')
        res = (res * (a - b)) % 31
    return res

# ans = "codes"

guesses = ["abcde", "fghij", "klmno", "pqrst", "uvwxy"]

with remote("betta.utctf.live", 7496) as conn:
    for attempt_idx in range(3):
        print("attempt idx", attempt_idx)

        # Get results for 5 guesses
        ress = []
        for guess in guesses:
            print(conn.recvline())
            conn.sendline(guess.encode())
            response = conn.recvline(keepends=False)
            res = int(response)
            ress.append(res)

        print("guesses", guesses)
        print("ress", ress)

        # Brute force words that produce the same results
        num_trials = 26 ** 5
        for trial_idx in range(num_trials):
            if trial_idx % 1_000_000 == 0:
                print("trial idx", trial_idx)

            trial_word = ""
            for i in range(5):
                char_idx = ( trial_idx // (26 ** (4 - i)) ) % 26
                char = chr(ord('a') + char_idx)
                trial_word += char
            
            is_candidate_ans = True
            for i in range(5):
                trial_res = get_res(guesses[i], trial_word)
                if trial_res != ress[i]:
                    is_candidate_ans = False
                    break
            if is_candidate_ans:
                print("candidate word", trial_word)
        print("done with candidates")
        
        print(conn.recvline())
        word = input("guess word ")
        conn.sendline(word.encode())
        line = conn.recvline()
        print(line)
        if not line.startswith(b"Good"):
            break
    
    line = conn.recvline()
    print(line)
    if line.startswith(b"Nice!"):
        line = conn.recvline()
        print(line)