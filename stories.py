"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}""")

story2 = Story(
    ["name", "relative_type", "noun", "vehicle", "adjective", "verb_ending_in_ing", "greeting"],
    """ Hello {name}, this is your {relative_type} calling. Just wanted to let you know you left your {noun} in my {vehicle} last night. I had a {adjective} time last night, never thought we'd end up {verb_ending_in_ing}. Love you, {greeting} """)

story3 = Story(
    ["location", "animal", "city", "business", "plural_noun", "acronym", "verb", "number", "adjective"],
    """ Breaking News! The {location} famous {animal} has escaped {city} zoo. It was last scene roaming the local {business} rummaging through old {plural_noun}. The {acronym}  team has been called in to {verb} the creature. So far there have only been {number} maimings and several {adjective} selfies taken  """)