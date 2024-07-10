from enum import Enum


class Endpoint(Enum):
    LABELS = "/rest/v2/labels/"
    SHARED_LABELS = "/rest/v2/labels/shared/"
    RENAME_SHARED_LABELS = "/rest/v2/labels/shared/rename"
    REMOVE_SHARED_LABELS = "/rest/v2/labels/shared/remove"

    #Comments
    COMMENTS = "/rest/v2/comments"

    # Tasks
    TASKS = "/rest/v2/tasks"
