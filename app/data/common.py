def bq(uz_question, ru_question, uz_options, ru_options, correct):
    return {
        "question": {"uz": uz_question, "ru": ru_question},
        "options": {
            key: {"uz": uz_options[key], "ru": ru_options[key]}
            for key in uz_options
        },
        "correct": correct,
    }
