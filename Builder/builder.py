"""
BUILDER PATTERN

What is Builder?
- Builder is a creational design pattern.
- It separates the construction of a complex object
  from the object that controls the construction process.
- The same construction process can create different
  representations.

Problem:
- Presentation currently knows how to build every
  output format:

      PdfDocument()
      Movie()

- It also knows format-specific details:

      pdf.add_page(...)
      movie.add_frame(...)

- If we add more formats, such as:

      IMAGE
      POWERPOINT

  we must modify Presentation.export().

- This violates the Open/Closed Principle.

Solution:
- Create a PresentationBuilder interface.
- Presentation only knows the construction step:

      builder.add_slide(slide)

- Concrete builders decide HOW each slide is added
  to their specific product.

Examples:

    PdfDocumentBuilder
        -> adds PDF pages

    MovieBuilder
        -> adds movie frames

Participants:

1. Product
   - PdfDocument
   - Movie

2. Builder
   - PresentationBuilder

3. Concrete Builders
   - PdfDocumentBuilder
   - MovieBuilder

4. Director
   - Presentation
   - Controls the construction process.

Flow:

    Presentation.export(builder)
              |
              v
      for each slide
              |
              v
      builder.add_slide(slide)
              |
        -----------------
        |               |
        v               v
   PDF Builder      Movie Builder
        |               |
        v               v
   add_page()       add_frame()

Key idea:

    Presentation knows WHAT steps to perform.

    Concrete builders know HOW to perform them.

Benefits:
- Presentation no longer depends on concrete products.
- New output formats can be added without modifying
  Presentation.
- Supports Open/Closed Principle.
- Construction logic is separated from the product.
"""


from abc import ABC, abstractmethod


# ==================================================
# SLIDE
# ==================================================

class Slide:

    def __init__(self, text: str):
        self.__text = text

    def get_text(self) -> str:
        return self.__text


# ==================================================
# PRODUCT - PDF
# ==================================================

class PdfDocument:

    def add_page(self, text: str):
        print(f"Adding PDF page: {text}")


# ==================================================
# PRODUCT - MOVIE
# ==================================================

class Movie:

    def add_frame(self, text: str, duration: int):
        print(
            f"Adding movie frame: {text}, "
            f"duration = {duration} seconds"
        )


# ==================================================
# BUILDER
# ==================================================

class PresentationBuilder(ABC):

    @abstractmethod
    def add_slide(self, slide: Slide):
        pass


# ==================================================
# CONCRETE BUILDER - PDF
# ==================================================

class PdfDocumentBuilder(PresentationBuilder):

    def __init__(self):
        self.__document = PdfDocument()

    def add_slide(self, slide: Slide):
        self.__document.add_page(
            slide.get_text()
        )

    def get_document(self) -> PdfDocument:
        return self.__document


# ==================================================
# CONCRETE BUILDER - MOVIE
# ==================================================

class MovieBuilder(PresentationBuilder):

    def __init__(self):
        self.__movie = Movie()

    def add_slide(self, slide: Slide):
        self.__movie.add_frame(
            slide.get_text(),
            3
        )

    def get_movie(self) -> Movie:
        return self.__movie


# ==================================================
# DIRECTOR
# ==================================================

class Presentation:

    def __init__(self):
        self.__slides: list[Slide] = []

    def add_slide(self, slide: Slide):
        self.__slides.append(slide)

    def export(self, builder: PresentationBuilder):

        for slide in self.__slides:
            builder.add_slide(slide)


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    presentation = Presentation()

    presentation.add_slide(
        Slide("Introduction")
    )

    presentation.add_slide(
        Slide("Design Patterns")
    )

    presentation.add_slide(
        Slide("Conclusion")
    )

    print("PDF EXPORT")
    print("----------")

    pdf_builder = PdfDocumentBuilder()

    presentation.export(pdf_builder)

    pdf = pdf_builder.get_document()

    print()

    print("MOVIE EXPORT")
    print("------------")

    movie_builder = MovieBuilder()

    presentation.export(movie_builder)

    movie = movie_builder.get_movie()
