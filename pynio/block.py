class Block(object):

    def __init__(self, name, type, config=None, instance=None):
        self._name = name
        self._type = type
        self.config = config or {}
        self._instance = instance

    def save(self, instance=None):
        """ PUTs the block config to nio.

        Will create a new block if one does not exist by this name.
        Otherwise it will update the existing block config.
        """

        # Add block to an instance if one is specified
        if instance:
            self._instance = instance

        if self._instance is None:
            raise Exception('Block is not associated with an instance')

        config = self.config
        config['name'] = self._name
        config['type'] = self._type
        self._put('blocks/{}'.format(self._name), config)
        if self._name not in self._instance.blocks:
            self._instances.blocks[self._name] = self
        assert self._instance.blocks[self._name] is self

    def _put(self, endpoint, config):
        self._instance._put(endpoint, config)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        print('You cannot change this attribute.')
        pass

    @property
    def type(self):
        return self._type
