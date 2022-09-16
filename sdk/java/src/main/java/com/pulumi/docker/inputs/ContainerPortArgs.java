// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.docker.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ContainerPortArgs extends com.pulumi.resources.ResourceArgs {

    public static final ContainerPortArgs Empty = new ContainerPortArgs();

    /**
     * Port exposed out of the container. If not given a free random port `&gt;= 32768` will be used.
     * 
     */
    @Import(name="external")
    private @Nullable Output<Integer> external;

    /**
     * @return Port exposed out of the container. If not given a free random port `&gt;= 32768` will be used.
     * 
     */
    public Optional<Output<Integer>> external() {
        return Optional.ofNullable(this.external);
    }

    /**
     * Port within the container.
     * 
     */
    @Import(name="internal", required=true)
    private Output<Integer> internal;

    /**
     * @return Port within the container.
     * 
     */
    public Output<Integer> internal() {
        return this.internal;
    }

    /**
     * IP address/mask that can access this port. Defaults to `0.0.0.0`.
     * 
     */
    @Import(name="ip")
    private @Nullable Output<String> ip;

    /**
     * @return IP address/mask that can access this port. Defaults to `0.0.0.0`.
     * 
     */
    public Optional<Output<String>> ip() {
        return Optional.ofNullable(this.ip);
    }

    /**
     * Protocol that can be used over this port. Defaults to `tcp`.
     * 
     */
    @Import(name="protocol")
    private @Nullable Output<String> protocol;

    /**
     * @return Protocol that can be used over this port. Defaults to `tcp`.
     * 
     */
    public Optional<Output<String>> protocol() {
        return Optional.ofNullable(this.protocol);
    }

    private ContainerPortArgs() {}

    private ContainerPortArgs(ContainerPortArgs $) {
        this.external = $.external;
        this.internal = $.internal;
        this.ip = $.ip;
        this.protocol = $.protocol;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ContainerPortArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ContainerPortArgs $;

        public Builder() {
            $ = new ContainerPortArgs();
        }

        public Builder(ContainerPortArgs defaults) {
            $ = new ContainerPortArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param external Port exposed out of the container. If not given a free random port `&gt;= 32768` will be used.
         * 
         * @return builder
         * 
         */
        public Builder external(@Nullable Output<Integer> external) {
            $.external = external;
            return this;
        }

        /**
         * @param external Port exposed out of the container. If not given a free random port `&gt;= 32768` will be used.
         * 
         * @return builder
         * 
         */
        public Builder external(Integer external) {
            return external(Output.of(external));
        }

        /**
         * @param internal Port within the container.
         * 
         * @return builder
         * 
         */
        public Builder internal(Output<Integer> internal) {
            $.internal = internal;
            return this;
        }

        /**
         * @param internal Port within the container.
         * 
         * @return builder
         * 
         */
        public Builder internal(Integer internal) {
            return internal(Output.of(internal));
        }

        /**
         * @param ip IP address/mask that can access this port. Defaults to `0.0.0.0`.
         * 
         * @return builder
         * 
         */
        public Builder ip(@Nullable Output<String> ip) {
            $.ip = ip;
            return this;
        }

        /**
         * @param ip IP address/mask that can access this port. Defaults to `0.0.0.0`.
         * 
         * @return builder
         * 
         */
        public Builder ip(String ip) {
            return ip(Output.of(ip));
        }

        /**
         * @param protocol Protocol that can be used over this port. Defaults to `tcp`.
         * 
         * @return builder
         * 
         */
        public Builder protocol(@Nullable Output<String> protocol) {
            $.protocol = protocol;
            return this;
        }

        /**
         * @param protocol Protocol that can be used over this port. Defaults to `tcp`.
         * 
         * @return builder
         * 
         */
        public Builder protocol(String protocol) {
            return protocol(Output.of(protocol));
        }

        public ContainerPortArgs build() {
            $.internal = Objects.requireNonNull($.internal, "expected parameter 'internal' to be non-null");
            return $;
        }
    }

}