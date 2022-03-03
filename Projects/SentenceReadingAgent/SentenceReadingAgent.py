import common_words_categories
import re

class FrameSentence:
    def __init__(self, subjects: list, verb: str, noun: str = None, noun_adjectives: list = None, recipient: str = None,
                 location: str = None, time: str = None, quantities: str = None):
        self.subjects = subjects
        self.verb = verb
        self.noun = noun
        self.noun_adjectives = noun_adjectives
        self.recipient = recipient
        self.location = location
        self.time = time
        self.quantities = quantities

    def __str__(self):
        return f"subjects words: {self.subjects}, verb: {self.verb}, noun: {self.noun}," \
               f" noun_adjectives: {self.noun_adjectives}, recipent: {self.recipient}," \
               f" location: {self.location}, time: {self.time}, quantities: {self.quantities}"
class FrameQuestion:
    def __init__(self, question_words: list, subjects: list, noun: str):
        self.question_words = question_words
        self.subjects = subjects
        self.noun = noun

    def __str__(self):
        return f"question words: {self.question_words}, subjects: {self.subjects}, noun: {self.noun}"


def string_to_question_frame(question: str) -> FrameQuestion:
    question = question.rstrip("?")
    question = question.replace("'", "")
    words = question.split()

    question_words = []
    for word_index, word in enumerate(words):
        if word in common_words_categories.verbs or word in common_words_categories.other:
            question_words = words[:word_index]
            break

    last_word = words[len(words) - 1]
    if last_word in common_words_categories.prepositions:
        question_words.append(last_word)

    subjects = []
    for word_index, word in enumerate(words):
        if word in common_words_categories.names:
            subjects.append(word)
            if word_index + 2 < len(words) and words[word_index + 1] == "and":
                subjects.append(words[word_index + 2])
            break

    noun = None
    for word_index, word in enumerate(words):
        if word in common_words_categories.articles:
            noun = words[word_index + 1]
            break

    return FrameQuestion(question_words=question_words, subjects=subjects, noun=noun)






def answer_question(question_frame: FrameQuestion, sentence_frame: FrameSentence) -> str:
    if "Who" in question_frame.question_words:
        if len(question_frame.question_words) == 1:
            return sentence_frame.subjects[0]
        elif "with" in question_frame.question_words:
            subject1 = sentence_frame.subjects[0]
            subject2 = sentence_frame.subjects[1]
            if subject1 in question_frame.subjects:
                return subject2
            return subject1
        elif "to" in question_frame.question_words:
            if sentence_frame.recipient:
                return sentence_frame.recipient
            else:
                return sentence_frame.subjects[0]

    if "What" in question_frame.question_words:
        if len(question_frame.question_words) > 1 and len(sentence_frame.noun_adjectives) > 0:
            return sentence_frame.noun_adjectives[0]
        elif sentence_frame.noun is None:
            return str(" ".join(sentence_frame.subjects))
        return sentence_frame.noun

    if "How" in question_frame.question_words:
        if len(question_frame.question_words) == 1:
            return sentence_frame.verb
        if "far" in question_frame.question_words:
            return sentence_frame.noun
        if "much" in question_frame.question_words:
            return sentence_frame.quantities
        return sentence_frame.noun_adjectives[0]

    if "Where" in question_frame.question_words:
        return sentence_frame.location

    if "time" in question_frame.question_words:
        return sentence_frame.time

    return ""


def string_to_question_frame(question: str) -> FrameQuestion:
    question = question.rstrip("?")
    question = question.replace("'", "")
    words = question.split()

    question_words = []
    for word_index, word in enumerate(words):
        if word in common_words_categories.verbs or word in common_words_categories.other:
            question_words = words[:word_index]
            break

    last_word = words[len(words) - 1]
    if last_word in common_words_categories.prepositions:
        question_words.append(last_word)

    subjects = []
    for word_index, word in enumerate(words):
        if word in common_words_categories.names:
            subjects.append(word)
            if word_index + 2 < len(words) and words[word_index + 1] == "and":
                subjects.append(words[word_index + 2])
            break

    noun = None
    for word_index, word in enumerate(words):
        if word in common_words_categories.articles:
            noun = words[word_index + 1]
            break

    return FrameQuestion(question_words=question_words, subjects=subjects, noun=noun)


def string_to_sentence_frame(sentence: str) -> FrameSentence:
    sentence = sentence.rstrip('.')
    sentence = sentence.replace("'", "")
    words = sentence.split()

    subjects = []
    last_subject_index = 0
    for word_index, word in enumerate(words):
        if word in common_words_categories.names or word in common_words_categories.pronouns:
            subjects.append(word)
            last_subject_index = word_index
            if word_index + 2 < len(words) and words[word_index + 1] == "and":
                subjects.append(words[word_index + 2])
                last_subject_index = word_index + 2
            break

    if len(subjects) == 0:
        for word_index, word in enumerate(words):
            if word.lower() in common_words_categories.articles:
                if word_index + 3 < len(words) and words[word_index + 2] == "of":
                    subjects = words[word_index + 1:word_index + 4]
                    last_subject_index = word_index + 3
                else:
                    subjects.append(words[word_index + 1])
                    last_subject_index = word_index + 1
                break

    verb = words[last_subject_index + 1] if last_subject_index + 1 < len(words) else None

    noun = None
    noun_adjectives = []

    for word_index, word in enumerate(words):
        if word in common_words_categories.articles or word in common_words_categories.quantities \
                or word in common_words_categories.numerals:
            for index in range(word_index + 1, len(words)):
                if words[index] in common_words_categories.prepositions:
                    noun = words[index - 1]
                    noun_adjectives = words[word_index + 1: index - 1]
                    break
                elif index == len(words) - 1:
                    noun = words[index]
                    noun_adjectives = words[word_index + 1: index]
            break

    for word_index, word in enumerate(words):
        if word in common_words_categories.versions_of_to_be and word_index + 1 < len(words) and words[
            word_index + 1] in common_words_categories.adjectives:
            noun_adjectives = words[word_index + 1]

    time_regex = r"((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm]))"
    time_regex_result = re.search(time_regex, sentence)
    time = None
    if time_regex_result:
        time = time_regex_result.group(1)

    place = None
    for word_index, word in enumerate(words):
        if word in {'at', 'to', 'in'} and words[word_index + 1] not in common_words_categories.verbs:
            possible_place = ""
            for index in range(word_index + 1, len(words)):
                if words[index] in common_words_categories.nouns:
                    possible_place += words[index]
                    break
                else:
                    possible_place += words[index] + " "
            if possible_place != time:
                place = possible_place
                break

    recipient = None
    for word_index, word in enumerate(words):
        if word in {'to'} and word_index + 1 < len(words) and words[word_index + 1] in common_words_categories.names:
            recipient = words[word_index + 1]

    quantities = None
    for word in words:
        if word in common_words_categories.quantities:
            quantities = word

    return FrameSentence(subjects=subjects, verb=verb, noun=noun, noun_adjectives=noun_adjectives, recipient=recipient,
                         location=place, time=time, quantities=quantities)


class SentenceReadingAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass
    noun= {'Serena','Andrew','Bobbie','Cason','David','Farzana','Frank','Hannah','Ida','Irene','Jim','Jose','Keith','Laura','Lucy','Meredith','Nick','Ada','Yeeling','Yan'}
    yesnowords = ["can", "could", "would", "is", "does", "has", "was", "were", "had", "have", "did", "are", "will"]
    commonwords = ["the", "a", "an", "is", "are", "were", "."]
    questionwords = ["who", "what", "where", "when", "why", "how", "whose", "which", "whom"]

    def solve(self, sentence, question):
        sentence_frame = string_to_sentence_frame(sentence)
        sentence_frame = string_to_sentence_frame(sentence)
        question_frame = string_to_question_frame(question)
        answer = answer_question(question_frame, sentence_frame)
        return answer