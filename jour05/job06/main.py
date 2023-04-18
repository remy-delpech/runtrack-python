def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        elif note % 5 >= 3 and note >= 38:
            notes_arrondies.append(note + 5 - note % 5)
        else:
            notes_arrondies.append(note)
    return notes_arrondies

notes = [76, 83, 65, 92, 41, 58, 90, 72]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)