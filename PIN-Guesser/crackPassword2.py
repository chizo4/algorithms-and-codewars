import hashlib

def crack(inputHash):
    listOfAttemptedPINs = []

    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        listOfAttemptedPINs.append(f"{i}{j}{k}{l}{m}")

    for attemptedPIN in listOfAttemptedPINs:
        testedHash = hashlib.md5(attemptedPIN.encode("utf-8")).hexdigest()
        if testedHash == inputHash: return attemptedPIN
