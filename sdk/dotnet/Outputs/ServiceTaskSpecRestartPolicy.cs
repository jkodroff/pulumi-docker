// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Docker.Outputs
{

    [OutputType]
    public sealed class ServiceTaskSpecRestartPolicy
    {
        /// <summary>
        /// Condition for restart: `(none|on-failure|any)`
        /// </summary>
        public readonly string? Condition;
        /// <summary>
        /// Delay between restart attempts `(ms|s|m|h)`
        /// </summary>
        public readonly string? Delay;
        /// <summary>
        /// Maximum attempts to restart a given container before giving up (default value is `0`, which is ignored)
        /// </summary>
        public readonly int? MaxAttempts;
        /// <summary>
        /// The time window used to evaluate the restart policy (default value is `0`, which is unbounded) `(ms|s|m|h)`
        /// </summary>
        public readonly string? Window;

        [OutputConstructor]
        private ServiceTaskSpecRestartPolicy(
            string? condition,

            string? delay,

            int? maxAttempts,

            string? window)
        {
            Condition = condition;
            Delay = delay;
            MaxAttempts = maxAttempts;
            Window = window;
        }
    }
}
