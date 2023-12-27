def retrieve_transaction_query(address, startTime, endTime, minValue, maxValue, reverse):
  return (
    f"""
      CALL ethereum.retrieve.transaction(
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

def retrieve_token_transfer_query(address, startTime, endTime, minValue, maxValue, reverse):
  return (
    f"""
      CALL ethereum.retrieve.tokenTransfer(
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
      CALL ethereum.graph.transaction(
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