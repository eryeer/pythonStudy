class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        mappings = dict()
        for key, value in attrs.items():
            if isinstance(value, tuple):
                print('found mapping %s==>%s' % (key, value))
                mappings[key] = value
        for key in mappings.keys():
            attrs.pop(key)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name

        return type.__new__(cls, name, bases, attrs)


class Model(object, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            if isinstance(getattr(self, k), str):
                args.append("""'%s'""" % getattr(self, k))
            else:
                args.append(str(getattr(self, k)))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(args))
        print(sql)


class User(Model):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")


u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
print(u.__dict__)
u.save()
