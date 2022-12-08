class LearningElement:
    def __init__(self, name, classification, ancestor_id, prerequisite_id, order_depth) -> None:
        self.name = name
        self.classification = classification
        self.ancestor_id = ancestor_id
        self.prerequisite_id = prerequisite_id
        self.order_depth = order_depth

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'classification': self.classification,
            'ancestor_id': self.ancestor_id,
            'prerequisite_id': self.prerequisite_id,
            'order_depth': self.order_depth
        }


class Module:
    def __init__(self, name) -> None:
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Topic:
    def __init__(self, name, module_id, ancestor_id, prerequisite_id, order_depth) -> None:
        self.name = name
        self.module_id = module_id
        self.ancestor_id = ancestor_id
        self.prerequisite_id = prerequisite_id
        self.order_depth = order_depth

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'module_id': self.module_id,
            'ancestor_id': self.ancestor_id,
            'prerequisite_id': self.prerequisite_id,
            'order_depth': self.order_depth
        }