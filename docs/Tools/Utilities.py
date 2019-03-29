"""Utilities used by the documentation scripts."""

import logging
import os

LOG = logging.getLogger(__name__)


def mkdir(folder):
  """Create a folder, ignore if it exists.

  :param str folder: folder to create
  """
  try:
    folder = os.path.join(os.getcwd(), folder)
    os.mkdir(folder)
  except OSError as e:
    LOG.debug('Exception when creating folder %s: %r', folder, e)


def writeLinesToFile(filename, lines):
  """Write a list of lines into a file.

  Checks that there are actual changes to be done.
  :param str filename: name of the files
  :param list lines: list of lines to write to the file
  """
  newContent = '\n'.join(lines)
  oldContent = None
  if os.path.exists(filename):
    with open(filename, 'r') as oldFile:
      oldContent = ''.join(oldFile.readlines())
  if oldContent is None or oldContent != newContent:
    with open(filename, 'w') as rst:
      LOG.info('Writing new content for %s', filename)
      rst.write(newContent)
  else:
    LOG.debug('Not updating file content for %s', filename)
