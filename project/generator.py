import random

project = ('continuous testing', 'continuous integration', 'continuous deployment', 'continuous improvement', 'devops')
adjectives = ('complete', 'modern', 'self-services', 'integrated', 'end-to-end')
verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')
adverbs = ('remarkably', 'enormously', 'substantially', 'significantly',
    'seriously')

def sample(l, n = 1): 
 result = random.sample(l, n)
 if n == 1:
  return result[0]
 return result

def generate_project():
 project_terms = sample(project, 2) 
 phrase = ' '.join([sample(adjectives), project_terms[0], sample(adverbs),
 	sample(verbs), project_terms[1]])
 return phrase.title()

if __name__ == "__main__":
	generate_project()
	op = generate_project()
	print(op)