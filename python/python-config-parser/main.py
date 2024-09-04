import configparser
config = configparser.ConfigParser()

#  config.read('example1.ini')
config.read('example2.ini')

print(config)

print(config.sections())

print(config['logger'].__class__)

print(dict(config))

for key, sec in dict(config).items():
    print(key, dict(sec))

print()

#  for key, opt in dict(config['All Values Are Strings']).items():
    #  print(key, opt, type(opt), sep='\t')

#  print()

#  for key in config.options('All Values Are Strings'):
    #  opt = config.get('All Values Are Strings', key, raw=False)
    #  print(key, opt, type(opt), sep='\t')

#  print()

#  print(dict(config.items('Sections Can Be Indented')))

for key in config.sections():
    print(key, dict(config.items(key)))


print(config.getboolean("logger.emblaze", "propagate"))
print(config.getboolean("logger.emblaze", "propagate", vars={"propagate": "no"}))
print(config['logger.emblaze'].getboolean("propagate"))

print(config.options("logger.emblaze"))
