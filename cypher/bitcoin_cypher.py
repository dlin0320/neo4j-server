def retrieve_transaction(address, startTime, endTime, minValue, maxValue, reverse):
  return (
    f"""
      CALL bitcoin.retrieve.transaction(
        "{address}",
        null,
        {startTime},
        {endTime},
        {minValue},
        {maxValue},
        {reverse}
      )
      YIELD result
      RETURN result
    """
)