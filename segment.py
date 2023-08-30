from vertex import Vertex
from segment_bounding_box import SegmentBoundingBox
from utils import url_to_id


class Segment:
    def __init__(self,
                 user: str,
                 filepath: str = None,
                 url: str = None,
                 feature: str = None):

        self._user = user
        self._filepath = filepath

        self._vertices = []
        self._bounding_box = None
        self._polygon = None

        self.url = url
        self.feature = feature

    @property
    def db_id(self):
        return url_to_id(self.url)

    @property
    def feature_db_id(self):
        return url_to_id(self.feature)

    def to_dict(self):
        return {
            "url": self.url,
            "feature": self.feature,
            "user": self._user,
            "filepath": self._filepath
        }

    def load_children(self, repository):
        self._vertices = repository.get_vertices_for_segment(self.db_id)
        self._bounding_box = repository.get_bounding_box_for_segment(self.db_id)
        self._filepath = self._bounding_box.filepath if self._bounding_box is not None else None
        self._polygon = self._build_polygon(self._vertices)

    @property
    def user(self) -> str:
        return self._user

    @property
    def is_complete(self) -> bool:
        is_complete = False

        if len(self._vertices) > 3:
            is_complete = True

        return is_complete

    @property
    def vertices(self) -> list[Vertex]:
        return self._sort_vertices_by_order(self._vertices)

    @vertices.setter
    def vertices(self, vertices: list[Vertex]):
        self._vertices = self._sort_vertices_by_order(vertices)

    @property
    def polygon(self) -> Polygon:
        return self._build_polygon(self.vertices)

    @property
    def bounding_box(self) -> SegmentBoundingBox:
        return self._generate_bounding_box(self.polygon)

    @property
    def filepath(self) -> str:
        return self._filepath

    def set_filepath(self, filepath: str) -> None:
        self._filepath = filepath

        if self._bounding_box is not None:
            self._bounding_box.filepath = self._filepath

    def add_vertex(self, vertex: Vertex) -> None:
        self._vertices.append(vertex)

        # Whenever new vertex is added, polygon needs to be rebuilt and bounding box needs to be resized for new polygon
        self._polygon = self._build_polygon(self.vertices)
        self._bounding_box = self._generate_bounding_box(self._polygon)

    def _build_polygon(self, vertices: list[Vertex]) -> Polygon:
        polygon = None

        if len(vertices) > 2:
            all_coordinates = []
            for vertex in vertices:
                vertex_2D_coordinates = (vertex.x, vertex.y)
                all_coordinates.append(vertex_2D_coordinates)

            polygon = Polygon(all_coordinates)

        return polygon

    def _generate_bounding_box(self, polygon: Polygon) -> SegmentBoundingBox:
        bounding_box = None
        bounding_box_db_id = self._bounding_box.db_id if self._bounding_box is not None else None

        if polygon is not None:
            bounds = polygon.bounds
            bounding_box = SegmentBoundingBox(int(bounds[0]),
                                              int(bounds[1]),
                                              int(bounds[2]),
                                              int(bounds[3]),
                                              self._filepath,
                                              db_id=bounding_box_db_id,
                                              segment_db_id=self.db_id)

        return bounding_box

    def clear_vertices(self) -> None:
        self._vertices = []
        self._bounding_box = None
        self._polygon = None

    def fetch_vertices(self) -> None:

        if self.db_id is None:
            raise DbIdException(missing_db_id_field='segment id')
        else:
            self._vertices = VertexRepo().get_vertices_for_segment(self.db_id)

    def _sort_vertices_by_order(self, vertices: list[Vertex]) -> list[Vertex]:
        ordered_vertices = sorted(vertices, key=lambda vertex: vertex.order)
        return ordered_vertices

    def _arrange_vertices_counterclockwise(self, vertices: list[Vertex]) -> list[Vertex]:

        if len(vertices) < 3:
            return []

        # Find center
        x_sum = 0
        y_sum = 0
        for vertex in vertices:
            x_sum += vertex.x
            y_sum += vertex.y

        num_vertices = len(vertices)
        center = ((x_sum / num_vertices), (y_sum / num_vertices))

        # Calculate arctan for each point against centerpoint
        vertices_angle_pairs = []
        for vertex in vertices:
            angle = np.arctan2(vertex.x-center[0], vertex.y-center[1])
            vertices_angle_pairs.append({'angle': angle,
                                         'vertex': vertex})

        # Sort the angles to achieve counterclockwise order
        vertices_angle_pairs = sorted(vertices_angle_pairs, key=lambda pair: pair['angle'])
        counterclockwise_vertices = [pair['vertex'] for pair in vertices_angle_pairs]

        # For visualization
        #fix, ax = plt.subplots()
        #ax.scatter([vertex.x for vertex in counterclockwise_vertices], [vertex.y for vertex in counterclockwise_vertices])
        #for index in range(len(counterclockwise_vertices)):
        #    x = counterclockwise_vertices[index].x
        #    y = counterclockwise_vertices[index].y
        #    ax.annotate(str(index), (x, y))
#
        #ax.plot(center[0], center[1], 'ro')

        return counterclockwise_vertices

