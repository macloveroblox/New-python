survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"]
]

language_sets = [set(languages) for languages in survey_results]
language_counts = {}

for languages in language_sets:
    for language in languages:
        language_counts[language] = language_counts.get(language, 0) + 1

chosen_by_all = set.intersection(*language_sets)

chosen_by_one = {
    language for language, count in language_counts.items() if count == 1
}

unique_language_count = len(language_counts)

chosen_by_two = {
    language for language, count in language_counts.items() if count == 2
}

participants_by_languages = {}
for participant_number, languages in enumerate(language_sets, start=1):
    participants_by_languages.setdefault(frozenset(languages), []).append(
        participant_number
    )

same_favorites = [
    participants
    for participants in participants_by_languages.values()
    if len(participants) > 1
]

print("Languages chosen by all participants:", sorted(chosen_by_all))
print("Languages chosen by one participant:", sorted(chosen_by_one))
print("Number of unique languages:", unique_language_count)
print("Languages chosen by exactly two participants:", sorted(chosen_by_two))
print("Participants with the same favorite languages:", same_favorites)
