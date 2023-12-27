def retrieve_transaction_query(address, startTime, endTime, minValue, maxValue, reverse):
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

def graph_transaction_query(address, timespan, maxRelationshipCount, startTime, endTime, minValue, maxValue, depth, reverse):
  return (
    f"""
      CALL bitcoin.graph.transaction(
        "{address}",
        {timespan},
        {maxRelationshipCount},
        {startTime},
        {endTime},
        {minValue},
        {maxValue},
        {depth},
        {reverse}
      )
      YIELD result
      RETURN result
    """
  )