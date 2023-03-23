# After verification stage, we will work on the solution optimization
import InOutFunctions as iof
import UpdateFunctions as uf
import utils
import EnlargeCommunity as ec


def Merge():
    # Load samples and settings
    samples, settings = utils.loadSettings()

    # Verify samples iteratively
    for s in samples:

        # Load verification result
        G_primitive, S_bounds, primitive_only, ConstraintType, constraint, loop_free, priority, out_path, _, target_n, timestep = utils.loadData(s, settings)
        VerifyResult = iof.loadVerifySolution(out_path, s)
        CommunityNumToNodes = uf.mapCommunityToNodes(VerifyResult)

        # If the number of current communities is smaller than target number, return.
        if len(CommunityNumToNodes) < target_n:
            print("Verification solution is good enough according to the target number of communities!")
            continue

        # If the number of target n can never achieve because S_bound[1] is too small, return error
        if S_bounds[1] * target_n < len(G_primitive.nodes()):
            print("The upper bound of one community make it impossible to get target_n communities to take all the nodes in this graph!")
            continue

        # Start merging from the community with the least incoming or outgoing edges.
        print("Now try merging the communities!")
        MergeResult, MergeFlag, MergeErrorLog = ec.enlargeCommunityMerge(G_primitive, S_bounds, ConstraintType,
                            constraint, loop_free, priority, timestep, VerifyResult, target_n)

        print(MergeResult, MergeFlag, MergeErrorLog)
        if MergeFlag:
            print("Merge passed according to the target N!")

            # Write current merge solution into a output file
            iof.writeSolution(out_path, '/sol_after_merge.txt', G_primitive, MergeResult)
        else:
            iof.reportMergeIssue(out_path, MergeResult, ErrorLog, timestep, VerifyResult)
Merge()